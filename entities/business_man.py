import osintbuddy as ob
from osintbuddy.elements import TextInput


class BusinessMan(ob.Plugin):
    label = "Business Man"
    color = "#22C55E99"
    icon = "tie"
    author = "OSIB"
    description = "Represent a businessman or professional."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Company", icon="building"),
        TextInput(label="Role", icon="id"),
    ]

