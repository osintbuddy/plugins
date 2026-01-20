import osintbuddy as ob
from osintbuddy.elements import TextInput


class Device(ob.Plugin):
    version = "1.0.0"
    label = "Device"
    category = "Devices"
    color = "#94A3B899"
    icon = "device-mobile"
    author = "OSIB"
    description = "Represent a generic device."

    elements = [
        TextInput(label="Identifier", icon="hash"),
        TextInput(label="Type", icon="tag"),
        TextInput(label="Owner", icon="user"),
    ]

