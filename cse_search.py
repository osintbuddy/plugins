import json, re, random, asyncio
from typing import Optional
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import httpx

from osintbuddy.elements import TextInput, DropdownInput
from osintbuddy.errors import PluginError
import osintbuddy as ob
import requests

cse_link_options = []
try:
    # import requests
    resp = requests.get('https://gist.githubusercontent.com/jerlendds/741d110f59a7d2ed2098325d30b00569/raw/25c15621eb67845db4ad65fc4ea8d3ad0991356f/cses.json')
    cse_link_options = json.loads(resp.text)
    # cse_link_options = []
except Exception as e:
    pass
    cse_link_options = []
    # print('Error loading CSE categories!', e)


class GoogleCSESearch(ob.Plugin):
    label = "CSE Search"

    description = 'Search through hundreds of categorized custom search engines from Google'
    author = "OSIB"
    icon = "world-search"
    color = "#78C84166"
    elements = [
        [
            TextInput(label="Query", icon="search"),
            DropdownInput(label="Max Results", value={"label": "100"}, options=[
                { "label": "10" },
                { "label": "20" },
                { "label": "30" },
                { "label": "40" },
                { "label": "50" },
                { "label": "60" },
                { "label": "70" },
                { "label": "80" },
                { "label": "90" },
                { "label": "100" }
            ]),
        ],
        DropdownInput(label="CSE Categories", options=cse_link_options)
    ]

    @ob.transform(label="To cse results", icon="search")
    async def to_cse_results(self, entity):
        if not entity.cse_categories:
            raise PluginError('The CSE Category field is required to transform.')
        cse_results = await self.get_cse_results(entity.query, entity.cse_categories, entity.max_results)
        return await self._map_cse_to_blueprint(cse_results)

    async def _map_cse_to_blueprint(self, resp):
        entities = []
        cse_search_result = await ob.Registry.get_plugin('cse_result')
        if results := resp.get("results"):
            for result in results:
                breadcrumb = result.get("breadcrumbUrl", {})
                blueprint = cse_search_result.create(
                    title=result.get("titleNoFormatting"),
                    content=result.get("contentNoFormatting"),
                    breadcrumb=f"{breadcrumb.get('host')} {' '.join(breadcrumb.get('crumbs', []))}",
                    url=result.get("unescapedUrl"),
                    cache_url=result.get("cacheUrl"),
                )
                entities.append(blueprint)
        return entities

    async def get_cse_results(self, query, url, max_results=100):
        parsed_url = urlparse(url)
        url_params = parse_qs(parsed_url.query)
        cx_param = url_params["cx"][0]

        # Robust JSONP parser
        def parse_jsonp(text: str, expected_callback: Optional[str] = None):
            try:
                if expected_callback and text.strip().startswith(expected_callback):
                    # Fallback to generic parsing below
                    pass
                # Find first '(' and last ')' and parse inside
                start = text.find('(')
                end = text.rfind(')')
                if start == -1 or end == -1 or end <= start:
                    raise ValueError('Invalid JSONP payload')
                return json.loads(text[start + 1 : end])
            except Exception as e:
                raise PluginError(f'Failed to parse CSE JSONP: {e}')

        # Use simple capture groups (avoid variable-length look-behind)
        re_token = re.compile(r'"cse_token"\s*:\s*"([^"]+)"')
        re_exp = re.compile(r'"exp"\s*:\s*(\[[^\]]*\])')
        re_cse_lib_version = re.compile(r'"cselibVersion"\s*:\s*"([^"]+)"')

        referer = f"https://cse.google.com/cse?cx={cx_param}"
        base_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
        }
        script_headers = {
            **base_headers,
            'Referer': referer,
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        async with httpx.AsyncClient(http2=True, headers=base_headers, timeout=30.0) as client:
            # Prime cookies and session by visiting the CSE page first (helps avoid automated-block page)
            try:
                await client.get(referer, headers={
                    **base_headers,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'cross-site',
                })
            except Exception:
                pass

            # 1) Fetch cse.js to extract token, exp and lib version
            js_url = f"https://cse.google.com/cse.js?cx={cx_param}"
            js_resp = await client.get(js_url, headers=script_headers)
            js_text = js_resp.text or ''

            if 'We\'re sorry' in js_text or js_resp.headers.get('content-type','').startswith('text/html'):
                raise PluginError('Google CSE blocked the request while fetching token. Please retry later.')

            m_token = re_token.search(js_text)
            m_exp = re_exp.search(js_text)
            m_lib = re_cse_lib_version.search(js_text)
            if not (m_token and m_exp and m_lib):
                raise PluginError('Failed to extract CSE session parameters from cse.js')

            cse_token = m_token.group(1)
            exp = m_exp.group(1)
            cse_lib_version = m_lib.group(1)

            # tiny human-like pause before querying results
            try:
                await asyncio.sleep(random.uniform(0.15, 0.35))
            except Exception:
                pass

            # 2) Fetch results from element API (JSONP)
            cb_value = f"{random.randint(1000, 9999)}"
            callback = "google.search.cse.api" + cb_value

            g_api_params = {
                # Align closer to browser requests to reduce suspicion
                'rsz': 20,
                'num': min(int(str(max_results)) if str(max_results).isdigit() else 20, 20),
                'hl': 'en',
                'source': 'gcsc',
                'gss': '.com',
                'cselibv': cse_lib_version,
                'cx': cx_param,
                'q': query or '',
                'safe': 'off',
                'cse_tok': cse_token,
                'sort': '',
                'exp': exp,
                'oq': query or '',
                'cseclient': 'hosted-page-client',
                'callback': callback,
                'rurl': referer,
            }

            cse_results_url = "https://cse.google.com/cse/element/v1?" + urlencode(g_api_params)
            res = await client.get(cse_results_url, headers=script_headers)
            text = res.text or ''

            # Detect block page and soft-retry with different callback once
            if 'We\'re sorry' in text or res.headers.get('content-type','').startswith('text/html'):
                # retry with a new callback token and no-cache param
                cb_value = f"{random.randint(10000, 99999)}"
                g_api_params['callback'] = "google.search.cse.api" + cb_value
                g_api_params['_'] = str(random.randint(1_000_000, 9_999_999))
                cse_results_url = "https://cse.google.com/cse/element/v1?" + urlencode(g_api_params)
                res = await client.get(cse_results_url, headers=script_headers)
                text = res.text or ''

            if 'We\'re sorry' in text or not text.strip():
                raise PluginError('Google CSE blocked the request. Try fewer requests or later.')

            try:
                cse_search_results = parse_jsonp(text, expected_callback=callback)
            except PluginError:
                # Fallback: try to slice conservatively
                i = text.find('{')
                j = text.rfind('}')
                if i != -1 and j != -1 and j > i:
                    cse_search_results = json.loads(text[i : j + 1])
                else:
                    raise

            return cse_search_results
