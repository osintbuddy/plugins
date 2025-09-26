import osintbuddy as ob
from osintbuddy.elements import TextInput


class DesktopComputer(ob.Plugin):
    label = "Desktop Computer"
    color = "#22D3EE99"
    icon = "device-desktop"
    author = "OSIB"
    description = "Represent a desktop computer asset."

    elements = [
        TextInput(label="Hostname", icon="device-desktop"),
        TextInput(label="IP Address", icon="map-pin"),
        TextInput(label="OS", icon="cpu"),
    ]

