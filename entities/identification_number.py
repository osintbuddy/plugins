import osintbuddy as ob
from osintbuddy.elements import TextInput


class IdentificationNumber(ob.Plugin):
    version = "1.0.0"
    label = "Identification Number"
    color = "#94A3B899"
    icon = "id"
    author = "OSIB"
    description = "Represent a government-issued ID number."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Number", icon="hash"),
        TextInput(label="Country", icon="flag"),
    ]

