import osintbuddy as ob
from osintbuddy.elements import TextInput


class GovernmentOfficial(ob.Plugin):
    label = "Government Official"
    color = "#60A5FA99"
    icon = "shield"
    author = "OSIB"
    description = "Represent a government official."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Agency", icon="building"),
        TextInput(label="Title", icon="id"),
    ]

