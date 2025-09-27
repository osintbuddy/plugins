import osintbuddy as ob
from osintbuddy.elements import TextInput


class IOCIndicator(ob.Plugin):
    version = "1.0.0"
    label = "IOC Indicator"
    color = "#F43F5E99"
    icon = "alert-triangle"
    author = "OSIB"
    description = "Represent an Indicator of Compromise (type/value)."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Value", icon="hash"),
    ]
