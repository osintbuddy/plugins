from urllib.parse import urlparse
from osintbuddy.elements import TextInput
import osintbuddy as ob


class URL(ob.Plugin):
    label = "URL"
    color = '#642CA9'
    entity = [
        TextInput(label="URL", icon="link"),
    ]
    author = "team@OSINTBuddy"
    icon = "link"

    @ob.transform(label="To website", icon="world-www")
    async def transform_to_website(self, node, **kwargs):
        print('ob.Registry.plugins: ', ob.Registry.plugins)
        website_entity = await ob.Registry.get_plugin('website')
        domain = urlparse(node.url).netloc
        return website_entity.create(domain=domain)
