import osintbuddy as ob
from osintbuddy.elements import TextInput


class PassportNumber(ob.Plugin):
    version = "1.0.0"
    label = "Passport Number"
    color = "#94A3B899"
    icon = "id"
    author = "OSIB"
    description = "Represent a passport number."

    elements = [
        TextInput(label="Number", icon="hash"),
        TextInput(label="Country", icon="flag"),
        TextInput(label="Name", icon="user"),
    ]

