import osintbuddy as ob
from osintbuddy.elements import TextInput


class Company(ob.Plugin):
    version = "1.0.0"
    label = "Company"
    color = "#F59E0B99"
    icon = "building"
    author = "OSIB"
    description = "Represent a company or organization entry."

    elements = [
        TextInput(label="Name", icon="building"),
        TextInput(label="Domain", icon="world-www"),
        TextInput(label="Country", icon="flag"),
    ]

