import osintbuddy as ob
from osintbuddy.elements import TextInput


class MeetingBusiness(ob.Plugin):
    version = "1.0.0"
    label = "Meeting Business"
    color = "#A78BFA99"
    icon = "briefcase"
    author = "OSIB"
    description = "Represent a business meeting."

    elements = [
        TextInput(label="Subject", icon="briefcase"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

