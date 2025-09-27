import osintbuddy as ob
from osintbuddy.elements import TextInput


class Child(ob.Plugin):
    version = "1.0.0"
    label = "Child"
    color = "#60A5FA99"
    icon = "baby"
    author = "OSIB"
    description = "Represent a child (basic demographics)."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Age", icon="calendar"),
    ]

