import osintbuddy as ob
from osintbuddy.elements import TextInput


class Region(ob.Plugin):
    label = "Region"
    color = "#60A5FA99"
    icon = "map"
    author = "OSIB"
    description = "Represent a geographic region."

    elements = [
        TextInput(label="Name", icon="map"),
        TextInput(label="Country", icon="flag"),
    ]

