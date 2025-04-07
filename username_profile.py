from osintbuddy.elements import TextInput
import osintbuddy as ob

class UsernameProfile(ob.Plugin):
    label = "Username Profile"
    is_available = False
    color = "#D842A6"
    icon = "user-scan"
    author = "OSIB"
    
    entity = [
        TextInput(label='Profile Link', icon='link'),
    ]

    @ob.transform(label="To URL", icon="link")
    async def transform_to_url(self, node, use):
        url_entity = await ob.Registry.get_plugin('url')
        url_node = url_entity.create(
            url=node.profile_link
        )
        return url_node
