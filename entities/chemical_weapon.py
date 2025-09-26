import osintbuddy as ob
from osintbuddy.elements import TextInput


class ChemicalWeapon(ob.Plugin):
    version = "1.0.0"
    label = "Chemical Weapon"
    color = "#F43F5E99"
    icon = "flask"
    author = "OSIB"
    description = "Represent a chemical weapon classification."

    elements = [
        TextInput(label="Agent", icon="flask"),
        TextInput(label="Designation", icon="tag"),
    ]

