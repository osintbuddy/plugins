import osintbuddy as ob
from osintbuddy.elements import TextInput


class Office(ob.Plugin):
    version = "1.0.0"
    label = "Office"
    category = "Locations"
    color = "#FDE04799"
    icon = "building"
    author = "OSIB"
    description = "Represent an office location."

    elements = [
        TextInput(label="Address", icon="home"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

