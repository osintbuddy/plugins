import osintbuddy as ob
from osintbuddy.elements import TextInput


class Missile(ob.Plugin):
    version = "1.0.0"
    label = "Missile"
    color = "#F9731699"
    icon = "rocket"
    author = "OSIB"
    description = "Represent a missile system."

    elements = [
        TextInput(label="Designation", icon="tag"),
        TextInput(label="Range", icon="ruler"),
        TextInput(label="Manufacturer", icon="building"),
    ]

