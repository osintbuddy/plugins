import osintbuddy as ob
from osintbuddy.elements import TextInput


class Organization(ob.Plugin):
    label = "Organization"
    color = "#F59E0B99"
    icon = "building"
    author = "OSIB"
    description = "Represent an organization entity."

    elements = [
        TextInput(label="Name", icon="building"),
        TextInput(label="Type", icon="tag"),
        TextInput(label="Country", icon="flag"),
    ]

