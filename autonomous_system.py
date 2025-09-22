import osintbuddy as ob
from osintbuddy.elements import TextInput


class AutonomousSystem(ob.Plugin):
    label = "Autonomous System"
    color = "#06B6D499"
    icon = "router"
    author = "OSIB"
    description = "Represent an Autonomous System (ASN)."

    elements = [
        TextInput(label="ASN", icon="router"),
        TextInput(label="Org", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

