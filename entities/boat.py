import osintbuddy as ob
from osintbuddy.elements import TextInput


class Boat(ob.Plugin):
    version = "1.0.0"
    label = "Boat"
    category = "Transportation"
    color = "#38BDF899"
    icon = "sailboat"
    author = "OSIB"
    description = "Represent a watercraft registration."

    elements = [
        TextInput(label="Registration", icon="hash"),
        TextInput(label="Make", icon="tool"),
        TextInput(label="Model", icon="tools"),
    ]

