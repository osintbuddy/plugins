import osintbuddy as ob
from osintbuddy.elements import TextInput


class GovernmentOfficial(ob.Plugin):
    version = "1.0.0"
    label = "Government Official"
    category = "Identity"
    color = "#60A5FA99"
    icon = "shield"
    author = "OSIB"
    description = "Represent a government official."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Agency", icon="building"),
        TextInput(label="Title", icon="id"),
    ]

