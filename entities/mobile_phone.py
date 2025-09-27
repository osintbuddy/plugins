import osintbuddy as ob
from osintbuddy.elements import TextInput


class MobilePhone(ob.Plugin):
    version = "1.0.0"
    label = "Mobile Phone"
    color = "#22C55E99"
    icon = "device-mobile"
    author = "OSIB"
    description = "Represent a mobile handset."

    elements = [
        TextInput(label="IMEI", icon="hash"),
        TextInput(label="OS", icon="cpu"),
        TextInput(label="Owner", icon="user"),
    ]

