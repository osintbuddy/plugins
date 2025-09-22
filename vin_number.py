import osintbuddy as ob
from osintbuddy.elements import TextInput


class VinNumber(ob.Plugin):
    label = "VIN Number"
    color = "#9CA3AF99"
    icon = "hash"
    author = "OSIB"
    description = "Represent a Vehicle Identification Number."

    elements = [
        TextInput(label="VIN", icon="hash"),
        TextInput(label="Make", icon="tool"),
        TextInput(label="Model", icon="tools"),
    ]

