import osintbuddy as ob
from osintbuddy.elements import TextInput


class Bus(ob.Plugin):
    version = "1.0.0"
    label = "Bus"
    category = "Transportation"
    color = "#A78BFA99"
    icon = "bus"
    author = "OSIB"
    description = "Represent a bus vehicle identifier."

    elements = [
        TextInput(label="VIN", icon="hash"),
        TextInput(label="Registration", icon="hash"),
        TextInput(label="Route", icon="road"),
    ]

