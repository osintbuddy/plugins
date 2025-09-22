import osintbuddy as ob
from osintbuddy.elements import TextInput


class Train(ob.Plugin):
    label = "Train"
    color = "#A78BFA99"
    icon = "train"
    author = "OSIB"
    description = "Represent a train identifier."

    elements = [
        TextInput(label="Operator", icon="building"),
        TextInput(label="Number", icon="hash"),
        TextInput(label="Route", icon="road"),
    ]

