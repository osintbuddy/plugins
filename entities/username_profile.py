from osintbuddy.elements import TextInput
from osintbuddy import Plugin


class UsernameProfile(Plugin):
    label = "Username Profile"
    is_available = False
    color = "#8d0a6199"
    icon = "user-scan"
    author = "OSIB"
    
    elements = [
        TextInput(label='Profile Link', icon='link'),
    ]
