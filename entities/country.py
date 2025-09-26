import osintbuddy as ob
from osintbuddy.elements import TextInput


class Country(ob.Plugin):
    version = "1.0.0"
    label = "Country"
    color = "#F59E0B99"
    icon = "flag"
    author = "OSIB"
    description = "Represent a country."

    elements = [
        TextInput(label="Name", icon="flag"),
        TextInput(label="ISO Code", icon="hash"),
        TextInput(label="Region", icon="map"),
    ]

