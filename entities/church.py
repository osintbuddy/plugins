import osintbuddy as ob
from osintbuddy.elements import TextInput


class Church(ob.Plugin):
    version = "1.0.0"
    label = "Church"
    category = "Organizations"
    color = "#A3E63599"
    icon = "building-church"
    author = "OSIB"
    description = "Represent a church or religious building."

    elements = [
        TextInput(label="Name", icon="building-church"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

