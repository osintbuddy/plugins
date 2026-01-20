from osintbuddy.elements import TextInput
from osintbuddy import Plugin


class UsernameProfile(Plugin):
    version = "1.0.0"
    label = "Username Profile"
    category = "Social Media"
    is_available = False
    color = "#8d0a6199"
    icon = "user-scan"
    author = "OSIB"
    
    elements = [
        TextInput(label='Profile Link', icon='link'),
    ]
