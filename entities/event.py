import osintbuddy as ob
from osintbuddy.elements import TextInput


class Event(ob.Plugin):
    version = "1.0.0"
    label = "Event"
    color = "#60A5FA99"
    icon = "calendar-event"
    author = "OSIB"
    description = "Represent an event occurrence."

    elements = [
        TextInput(label="Name", icon="calendar-event"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

