from osintbuddy.elements import TextInput
from osintbuddy import transform, Registry

@transform(
    target="username_profile@1.0.0",
    label="To URL",
    icon="link"
)
async def to_url(self, entity):
    url_entity = await Registry.get_plugin('url@1.0.0')
    url_node = url_entity.create(
        url=entity.profile_link
    )
    return url_node
