import osintbuddy as ob
from osintbuddy.elements import TextInput


class Prison(ob.Plugin):
    version = "1.0.0"
    label = "Prison"
    color = "#94A3B899"
    icon = "building-arch"
    author = "OSIB"
    description = "Represent a prison or detention facility."

    elements = [
        TextInput(label="Name", icon="building-arch"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

