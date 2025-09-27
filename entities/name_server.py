import osintbuddy as ob
from osintbuddy.elements import TextInput


class NameServer(ob.Plugin):
    version = "1.0.0"
    label = "Name Server"
    color = "#EF444499"
    icon = "server"
    author = "OSIB"
    description = "Represent a DNS nameserver (NS)."

    elements = [
        TextInput(label="NS Host", icon="server"),
        TextInput(label="IP Address", icon="map-pin"),
    ]

