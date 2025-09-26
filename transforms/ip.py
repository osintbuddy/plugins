import socket
import httpx
from selenium.webdriver.common.by import By
from osintbuddy import utils
from osintbuddy.errors import PluginError
from osintbuddy.utils import to_camel_case
import httpx
from osintbuddy import transform, Registry



@transform(target="ip@1.0.0", label="To website", icon="world")
async def to_website(self, entity):
    website_entity = await Registry.get_plugin('website@1.0.0')
    try:
        resolved = socket.gethostbyaddr(entity.ip_address)
        if len(resolved) >= 1:
            blueprint = website_entity.create(domain=resolved[0])
            return blueprint
        else:
            raise PluginError("No results found")
    except (socket.gaierror, socket.herror):
        raise PluginError("We ran into a socket error. Please try again")


@transform(target="ip@1.0.0", label="To subdomains", icon="world")
async def to_subdomains(self, entity):
    nodes = []
    params = {
        "q": entity.ip_address,
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                'https://api.hackertarget.com/reverseiplookup',
                params=params,
                timeout=None
            )
            data = response.content.decode("utf8").split("\n")
    except Exception as e:
        raise PluginError(e)
    subdomain_entity = await ob.Registry.get_plugin('subdomain')
    for subdomain in data:
        blueprint = subdomain_entity.create(subdomain=subdomain)
        nodes.append(blueprint)
    return nodes


@transform(target="ip@1.0.0", label="To geolocation", icon="map-pin")
async def to_geolocation(self, entity):
    summary_rows = [
        "ASN",
        "Hostname",
        "Range",
        "Company",
        "Hosted domains",
        "Privacy",
        "Anycast",
        "ASN type",
        "Abuse contact",
    ]
    geo_rows = [
        "City",
        "State",
        "Country",
        "Postal",
        "Timezone",
        "Coordinates",
    ]
    if len(entity.ip_address) == 0:
        raise PluginError(
            "A valid IP Address is a required field for this transform"
        )

    geolocation = {}
    summary = {}
    with utils.get_driver() as driver:
        driver.get(f'https://ipinfo.io/{entity.ip_address}')
        for row in summary_rows:
            summary[to_camel_case(row)] = driver.find_element(
                by=By.XPATH, value=self.get_summary_xpath(row)
            ).text
        for row in geo_rows:
            geolocation[to_camel_case(row)] = driver.find_element(
                by=By.XPATH, value=self.get_geo_xpath(row)
            ).text
    IPGeolocationPlugin = await Registry.get_plugin('ip_geolocation@1.0.0')
    blueprint = IPGeolocationPlugin.create(
        city=geolocation.get("city"),
        state=geolocation.get("state"),
        country=geolocation.get("country"),
        postal=geolocation.get("postal"),
        timezone=geolocation.get("timezone"),
        coordinates=geolocation.get("coordinates"),
        asn=summary.get("asn"),
        hostname=summary.get("hostname"),
        range=summary.get("range"),
        company=summary.get("company"),
        hosted_domains=summary.get("hostedDomains"),
        privacy=summary.get("privacy"),
        anycast=summary.get("anycast"),
        asn_type=summary.get("asnType"),
        abuse_contact=summary.get("abuseContact"),
    )
    return blueprint

def get_summary_xpath(value: str):
    return (
        f"//td//span[contains(text(),'{value}')]"
        "/ancestor::td/following-sibling::td"
    )

def get_geo_xpath(value: str):
    return f"//td[contains(text(),'{value}')]/following-sibling::td"
