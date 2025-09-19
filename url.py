from urllib.parse import urlparse
from osintbuddy.elements import TextInput
import osintbuddy as ob


class URL(ob.Plugin):
    label = "URL"
    color = '#47139699'
    elements = [
        TextInput(label="URL", icon="link"),
    ]
    author = "OSIB"
    icon = "link"
    description = "Uniform Resource Locator, usually starts with https://"

    @ob.transform(label="To website", icon="world-www")
    async def to_website(self, entity):
        print('ob.Registry.plugins: ', ob.Registry.plugins)
        website_entity = await ob.Registry.get_plugin('website')
        domain = urlparse(entity.url).netloc
        return website_entity.create(domain=domain)
