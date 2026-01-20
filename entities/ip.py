from osintbuddy import Plugin
from osintbuddy.elements import TextInput

class IP(Plugin):
    version = "1.0.0"
    label = "IP"
    category = "Network"
    color = "#E6521F99"
    elements = [TextInput(label="IP Address", icon="map-pin")]
    icon = "building-broadcast-tower"
    author = "OSIB"
    description = "Internet Protocol address"
