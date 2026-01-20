import osintbuddy as ob
from osintbuddy.elements import TextInput


class Plane(ob.Plugin):
    version = "1.0.0"
    label = "Plane"
    category = "Transportation"
    color = "#38BDF899"
    icon = "plane"
    author = "OSIB"
    description = "Represent an aircraft."

    elements = [
        TextInput(label="Tail Number", icon="hash"),
        TextInput(label="Model", icon="tools"),
        TextInput(label="Airline", icon="plane"),
    ]

