import osintbuddy as ob
from osintbuddy.elements import TextInput


class Blade(ob.Plugin):
    label = "Blade"
    color = "#94A3B899"
    icon = "knife"
    author = "OSIB"
    description = "Represent an edged weapon (knife/machete)."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Length", icon="ruler"),
        TextInput(label="Brand", icon="building"),
    ]

