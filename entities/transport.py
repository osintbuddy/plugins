import osintbuddy as ob
from osintbuddy.elements import TextInput


class Transport(ob.Plugin):
    label = "Transport"
    color = "#94A3B899"
    icon = "road"
    author = "OSIB"
    description = "Represent a transport item or reference."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Identifier", icon="hash"),
    ]

