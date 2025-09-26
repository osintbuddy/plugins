import osintbuddy as ob
from osintbuddy.elements import TextInput


class Smartphone(ob.Plugin):
    label = "Smartphone"
    color = "#22C55E99"
    icon = "device-mobile"
    author = "OSIB"
    description = "Represent a smartphone device."

    elements = [
        TextInput(label="IMEI", icon="hash"),
        TextInput(label="OS", icon="cpu"),
        TextInput(label="Owner", icon="user"),
    ]

