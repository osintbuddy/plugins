import osintbuddy as ob
from osintbuddy.elements import TextInput


class IED(ob.Plugin):
    label = "IED"
    color = "#F9731699"
    icon = "flame"
    author = "OSIB"
    description = "Represent an improvised explosive device."

    elements = [
        TextInput(label="Configuration", icon="settings"),
        TextInput(label="Trigger", icon="bolt"),
    ]

