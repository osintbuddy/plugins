import osintbuddy as ob
from osintbuddy.elements import TextInput


class Shodan(ob.Plugin):
    label = "Shodan"
    color = "#22C55E99"
    icon = "database-search"
    author = "OSIB"
    description = "Represent a Shodan query or result reference."

    elements = [
        TextInput(label="Query", icon="search"),
        TextInput(label="Host IP", icon="map-pin"),
    ]

