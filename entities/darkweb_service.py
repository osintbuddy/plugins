import osintbuddy as ob
from osintbuddy.elements import TextInput


class DarkwebService(ob.Plugin):
    version = "1.0.0"
    label = "Darkweb Service"
    category = "Web"
    color = "#6B728099"
    icon = "brand-tor"
    author = "OSIB"
    description = "Represent a darkweb/onion service reference."

    elements = [
        TextInput(label="Service Name", icon="ghost"),
        TextInput(label="Onion URL", icon="link"),
    ]
