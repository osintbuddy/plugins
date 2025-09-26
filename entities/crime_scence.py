import osintbuddy as ob
from osintbuddy.elements import TextInput


class CrimeScence(ob.Plugin):
    version = "1.0.0"
    label = "Crime Scence"
    color = "#EF444499"
    icon = "alert-triangle"
    author = "OSIB"
    description = "Represent a crime scene reference (location/time)."

    elements = [
        TextInput(label="Location", icon="map-pin"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Case ID", icon="hash"),
    ]

