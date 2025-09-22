import osintbuddy as ob
from osintbuddy.elements import TextInput


class City(ob.Plugin):
    label = "City"
    color = "#60A5FA99"
    icon = "building"
    author = "OSIB"
    description = "Represent a city."

    elements = [
        TextInput(label="Name", icon="building"),
        TextInput(label="Country", icon="flag"),
        TextInput(label="Region", icon="map"),
    ]

