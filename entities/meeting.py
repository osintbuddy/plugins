import osintbuddy as ob
from osintbuddy.elements import TextInput


class Meeting(ob.Plugin):
    version = "1.0.0"
    label = "Meeting"
    color = "#22C55E99"
    icon = "calendar"
    author = "OSIB"
    description = "Represent a generic meeting."

    elements = [
        TextInput(label="Topic", icon="calendar"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

