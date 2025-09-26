import osintbuddy as ob
from osintbuddy.elements import TextInput


class MeetingSocial(ob.Plugin):
    version = "1.0.0"
    label = "Meeting Social"
    color = "#FB718599"
    icon = "users"
    author = "OSIB"
    description = "Represent a social meeting or gathering."

    elements = [
        TextInput(label="Occasion", icon="users"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

