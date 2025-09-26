import osintbuddy as ob
from osintbuddy.elements import TextInput


class MobileComputer(ob.Plugin):
    version = "1.0.0"
    label = "Mobile Computer"
    color = "#22D3EE99"
    icon = "device-laptop"
    author = "OSIB"
    description = "Represent a laptop or tablet."

    elements = [
        TextInput(label="Hostname", icon="device-laptop"),
        TextInput(label="OS", icon="cpu"),
        TextInput(label="Owner", icon="user"),
    ]

