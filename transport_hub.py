import osintbuddy as ob
from osintbuddy.elements import TextInput


class TransportHub(ob.Plugin):
    label = "Transport Hub"
    color = "#9CA3AF99"
    icon = "building-stadium"
    author = "OSIB"
    description = "Represent a transport hub (airport/station/port)."

    elements = [
        TextInput(label="Name", icon="building"),
        TextInput(label="Type", icon="tag"),
        TextInput(label="City", icon="building"),
    ]

