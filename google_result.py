import osintbuddy as ob
from osintbuddy.elements import Title, CopyText
from urllib.parse import urlparse


class GoogleResult(ob.Plugin):
    label = "Google Result"
    is_available = False
    color = "#3D78D999"
    elements = [Title(label="result"), CopyText(label="url")]
    icon = "brand-google"
    author = "OSIB"

    @ob.transform(label="To website", icon="world")
    async def to_website(self, entity):
        website_entity = await ob.Registry.get_plugin('website')
        blueprint = website_entity.create(
            domain=urlparse(entity.url).netloc
        )
        return blueprint
