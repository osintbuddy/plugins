from osintbuddy.elements import TextInput
import osintbuddy as ob

class UsernameProfile(ob.Plugin):
    label = "Username Profile"
    is_available = False
    color = "#8d0a6199"
    icon = "user-scan"
    author = "OSIB"
    
    elements = [
        TextInput(label='Profile Link', icon='link'),
    ]

    @ob.transform(label="To URL", icon="link")
    async def to_url(self, entity):
        url_entity = await ob.Registry.get_plugin('url')
        url_node = url_entity.create(
            url=entity.profile_link
        )
        return url_node
