import osintbuddy as ob
from osintbuddy.elements import Title, CopyText
from urllib.parse import urlparse


class GoogleResult(ob.Plugin):
    label = "Google Result"
    is_available = False
    color = "#308e49"
    entity = [Title(label="result"), CopyText(label="url")]
    icon = "brand-google-filled"
    author = "OSIB"

    @ob.transform(label="To website", icon="world")
    async def transform_to_website(self, node, use):
        website_entity = await ob.Registry.get_plugin('website')
        blueprint = website_entity.create(
            domain=urlparse(node.url).netloc
        )
        return blueprint
