import osintbuddy as ob
from osintbuddy.elements import TextInput


class Harbor(ob.Plugin):
    version = "1.0.0"
    label = "Harbor"
    category = ["Locations", "Transportation"]
    color = "#38BDF899"
    icon = "anchor"
    author = "OSIB"
    description = "Represent a harbor or port location."

    elements = [
        TextInput(label="Name", icon="anchor"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

