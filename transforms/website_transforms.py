import socket
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from osintbuddy.elements import TextInput
from osintbuddy.errors import PluginError
from osintbuddy import transform, Registry, utils


def _parse_whois(whois_data):
    data = []
    for line in whois_data.split("\n"):
        if "DNSSEC" in line:
            data.append(line)
            break
        else:
            data.append(line)
    return data


@transform(
  target="website@1.0.0",
  label="To IP",
  icon="building-broadcast-tower"
)
async def to_ip(entity):
    ip_address_plugin = await Registry.get_entity('ip')
    blueprint = ip_address_plugin.create(
        ip_address=socket.gethostbyname(entity.domain),
    )
    return blueprint

@transform(target="website@1.0.0", label="To google", icon="world")
async def to_google(self, entity):
    results = []
    google_search_entity = await Registry.get_entity('google_search@1.0.0')
    for result in await google_search_entity().search_google(
        query=entity.domain, pages="3"
    ):
        google_result_entity = await Registry.get_entity('google_result@1.0.0')
        blueprint = google_result_entity.create(
            result={
                "title": result.get("title"),
                "subtitle": result.get("breadcrumb"),
                "text": result.get("description"),
            },
            url=result.get("url"),
        )
        results.append(blueprint)
    return results

@transform(target="website@1.0.0", label="To WHOIS", icon="world")
async def to_whois(entity):
    domain = entity.domain
    if len(domain.split(".")) > 2:
        domain = domain.split(".")
        domain = domain[len(domain) - 2] + "." + domain[len(domain) - 1]

    with utils.get_driver() as driver:
        driver.get(f"https://www.whois.com/whois/{domain}")
        raw_whois = ""
        try:
            raw_whois = driver.find_element(
                by=By.TAG_NAME, value="pre"
            ).text
        except Exception as e:
            print(e)
            raise PluginError(
                "Captcha encountered, please try again later."
            )
        whois_entity = await Registry.get_entity("whois")
        
        return whois_entity.create(
            whois_data="\n".join(_parse_whois(raw_whois)),
            raw_whois_data=raw_whois
        )


@transform(target="website@1.0.0", label="To DNS", icon="world")
async def to_dns(self, entity):
    dns_entity = await Registry.get_entity('dns')
    data = dns_entity.data_template()

    if len(entity.domain) == 0:
        raise PluginError(
            "A website is required to process dns records"
        )

    website = entity.domain
    website_parsed = urlparse(website)
    if website_parsed.scheme:
        domain = website_parsed.netloc
    else:
        domain = urlparse(f"https://{website}").netloc

    for key in data.keys():
        try:
            resolved = dns.resolver.resolve(domain, key)
            data[key] = [str(answer) for answer in resolved]
        except Exception:
            pass
    results = []
    data_filled = dict((k, v) for k, v in data.items() if v is not None)
    for key, value in data_filled.items():
        for entry in value:
            record_type = dns_entity.record(key, entry)
            record = record_type["text"]
            del record_type["text"]
            blueprint = dns_entity.create(
                record_type=record_type,
                value=record,
            )
            results.append(blueprint)
    return results
