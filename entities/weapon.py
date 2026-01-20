import osintbuddy as ob
from osintbuddy.elements import TextInput


class Weapon(ob.Plugin):
    version = "1.0.0"
    label = "Weapon"
    category = "Weapons"
    color = "#9CA3AF99"
    icon = "target"
    author = "OSIB"
    description = "Represent a weapon (generic)."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Make/Model", icon="tools"),
        TextInput(label="Serial", icon="hash"),
    ]

