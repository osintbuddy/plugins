import osintbuddy as ob
from osintbuddy.elements import TextInput


class Incident(ob.Plugin):
    label = "Incident"
    color = "#F59E0B99"
    icon = "alert-triangle"
    author = "OSIB"
    description = "Represent a security or criminal incident."

    elements = [
        TextInput(label="Case ID", icon="hash"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

