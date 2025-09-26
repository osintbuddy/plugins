import osintbuddy as ob
from osintbuddy.elements import TextInput


class Ports(ob.Plugin):
    version = "1.0.0"
    label = "Ports"
    color = "#0EA5E999"
    icon = "plug"
    author = "OSIB"
    description = "Represent a service port and protocol."

    elements = [
        TextInput(label="Port", icon="hash"),
        TextInput(label="Protocol", icon="plug"),
        TextInput(label="Service", icon="server"),
    ]
