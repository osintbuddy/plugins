import osintbuddy as ob
from osintbuddy.elements import TextInput


class ReligiousGroup(ob.Plugin):
    version = "1.0.0"
    label = "Religious Group"
    category = "Organizations"
    color = "#22C55E99"
    icon = "building-church"
    author = "OSIB"
    description = "Represent a religious group."

    elements = [
        TextInput(label="Name", icon="building-church"),
        TextInput(label="Country", icon="flag"),
        TextInput(label="Denomination", icon="tag"),
    ]

