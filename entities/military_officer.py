import osintbuddy as ob
from osintbuddy.elements import TextInput


class MilitaryOfficer(ob.Plugin):
    version = "1.0.0"
    label = "Military Officer"
    category = "Identity"
    color = "#60A5FA99"
    icon = "military-rank"
    author = "OSIB"
    description = "Represent a military officer."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Branch", icon="flag"),
        TextInput(label="Rank", icon="military-rank"),
    ]

