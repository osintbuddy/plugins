import osintbuddy as ob
from osintbuddy.elements import TextInput


class LawOfficer(ob.Plugin):
    version = "1.0.0"
    label = "Law Officer"
    category = "Identity"
    color = "#22C55E99"
    icon = "badge"
    author = "OSIB"
    description = "Represent a law enforcement officer."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Agency", icon="building"),
        TextInput(label="Badge Number", icon="id"),
    ]

