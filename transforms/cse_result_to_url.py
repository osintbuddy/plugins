from osintbuddy import transform, Registry

@transform(
    target='cse_result@1.0.0',
    label='To URL',
    icon='link',
)
async def to_url(self, entity):
    url_entity = await Registry.get_plugin('url@1.0.0')
    return url_entity.create(url=entity.url)
