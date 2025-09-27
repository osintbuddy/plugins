import osintbuddy as ob
from osintbuddy.elements import TextInput


class MacAddress(ob.Plugin):
    version = "1.0.0"
    label = "MAC Address"
    color = "#94A3B899"
    icon = "cpu"
    author = "OSIB"
    description = "Represent a device MAC address."

    elements = [
        TextInput(label="MAC", icon="hash"),
        TextInput(label="Vendor", icon="building"),
    ]

