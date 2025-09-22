import osintbuddy as ob
from osintbuddy.elements import TextInput


class Judge(ob.Plugin):
    label = "Judge"
    color = "#60A5FA99"
    icon = "gavel"
    author = "OSIB"
    description = "Represent a judge."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Court", icon="building"),
    ]

