from osintbuddy import Plugin
from osintbuddy.elements import TextInput

class IP(Plugin):
    label = "IP"
    color = "#E6521F99"
    elements = [TextInput(label="IP Address", icon="map-pin")]
    icon = "building-broadcast-tower"
    author = "OSIB"
    description = "Internet Protocol address"
