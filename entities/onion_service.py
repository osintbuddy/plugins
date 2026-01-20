import osintbuddy as ob
from osintbuddy.elements import TextInput


class OnionService(ob.Plugin):
    version = "1.0.0"
    label = "Onion Service"
    category = "Web"
    color = "#4B556399"
    icon = "brand-tor"
    author = "OSIB"
    description = "Represent a Tor hidden service (v3)."

    elements = [
        TextInput(label="Onion URL", icon="link"),
        TextInput(label="Category", icon="tag"),
    ]
