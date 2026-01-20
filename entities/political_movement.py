import osintbuddy as ob
from osintbuddy.elements import TextInput


class PoliticalMovement(ob.Plugin):
    version = "1.0.0"
    label = "Political Movement"
    category = "Organizations"
    color = "#60A5FA99"
    icon = "flag"
    author = "OSIB"
    description = "Represent a political movement."

    elements = [
        TextInput(label="Name", icon="flag"),
        TextInput(label="Country", icon="flag"),
        TextInput(label="Ideology", icon="tag"),
    ]

