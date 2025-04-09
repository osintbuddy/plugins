from osintbuddy.elements import Title, CopyText, Text
import osintbuddy as ob

class CSESearchResultsPlugin(ob.Plugin):
    label = "CSE Result"
    is_available = False
    color = "#058F63"
    icon = "brand-google"
    author = "OSIB"
    
    entity = [
        Title(label="title"),
        Text(label="breadcrumb"),
        Text(label="content"),
        CopyText(label="URL"),
        CopyText(label="Cache URL"),
    ]

    @ob.transform(label="To URL", icon='link')
    async def transform_to_url(self, node, **kwargs):
        url_entity = await ob.Registry.get_plugin('url')
        return url_entity.create(url=node.url)
