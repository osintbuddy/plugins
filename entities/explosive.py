import osintbuddy as ob
from osintbuddy.elements import TextInput


class Explosive(ob.Plugin):
    version = "1.0.0"
    label = "Explosive"
    color = "#F9731699"
    icon = "flame"
    author = "OSIB"
    description = "Represent an explosive material or device."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Weight", icon="scale"),
    ]

