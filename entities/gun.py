import osintbuddy as ob
from osintbuddy.elements import TextInput


class Gun(ob.Plugin):
    version = "1.0.0"
    label = "Gun"
    color = "#9CA3AF99"
    icon = "target"
    author = "OSIB"
    description = "Represent a firearm (make/model/serial)."

    elements = [
        TextInput(label="Make", icon="tool"),
        TextInput(label="Model", icon="tools"),
        TextInput(label="Serial Number", icon="hash"),
    ]

