from osintbuddy import Plugin
from osintbuddy.elements import TextInput

class GoogleSearch(Plugin):
    version = "1.0.0"
    label = "Google Search"
    category = "Search"
    color = "#3D78D999"
    elements = [
        TextInput(label="Query", icon="search"),
        TextInput(label="Pages", icon="123", value="3"),
    ]
    icon = "brand-google"
    author = "OSIB"
    description = "Search google using the advanced operators you're used to"
