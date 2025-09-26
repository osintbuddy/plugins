import osintbuddy as ob
from osintbuddy.elements import TextInput


class Male(ob.Plugin):
    label = "Male"
    color = "#60A5FA99"
    icon = "gender-male"
    author = "OSIB"
    description = "Represent a male person."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Age", icon="calendar"),
    ]

