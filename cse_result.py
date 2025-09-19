from osintbuddy.elements import Title, CopyText, Text
import osintbuddy as ob

class CSESearchResultsPlugin(ob.Plugin):
    label = "CSE Result"
    is_available = False
    color = "#59A12866"
    icon = "brand-google"
    author = "OSIB"
    
    elements = [
        Title(label="title"),
        Text(label="breadcrumb"),
        Text(label="content"),
        CopyText(label="URL"),
    ]

    @ob.transform(label="To URL", icon='link')
    async def to_url(self, entity):
        url_entity = await ob.Registry.get_plugin('url')
        return url_entity.create(url=entity.url)
