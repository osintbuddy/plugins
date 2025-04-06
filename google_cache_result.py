from urllib.parse import urlparse
from osintbuddy.elements import Title, CopyText
import osintbuddy as ob


class GoogleCacheResult(ob.Plugin):
    label = "Cache Result"
    is_available = False
    color = "#145070"
    entity = [
        Title(label="result", title="Some title"),
        [
            CopyText(label="URL"),
        ],
    ]
    icon = "brand-google-filled"
    author = "team@OSINTBuddy"

    @ob.transform(label="To website", icon="world-www")
    async def transform_to_website(self, node, use):
        WebsitePlugin = await ob.Registry.get_plugin('website')
        return WebsitePlugin.create(domain=urlparse(node.url).netloc)
