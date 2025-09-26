import osintbuddy as ob
from osintbuddy.elements import TextInput


class Airport(ob.Plugin):
    version = "1.0.0"
    label = "Airport"
    color = "#3B82F699"
    icon = "plane"
    author = "OSIB"
    description = "Represent an airport (IATA/ICAO codes and name)."

    elements = [
        TextInput(label="IATA", icon="letter-a"),
        TextInput(label="ICAO", icon="letter-i"),
        TextInput(label="Name", icon="map"),
        TextInput(label="Country", icon="flag"),
    ]
