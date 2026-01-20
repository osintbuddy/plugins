import osintbuddy as ob
from osintbuddy.elements import TextInput


class Ammunition(ob.Plugin):
    version = "1.0.0"
    label = "Ammunition"
    category = "Weapons"
    color = "#9CA3AF99"
    icon = "bullet"
    author = "OSIB"
    description = "Represent ammunition type and caliber."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Caliber", icon="ruler"),
        TextInput(label="Manufacturer", icon="building"),
    ]

