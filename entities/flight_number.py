import osintbuddy as ob
from osintbuddy.elements import TextInput


class FlightNumber(ob.Plugin):
    version = "1.0.0"
    label = "Flight Number"
    color = "#38BDF899"
    icon = "plane"
    author = "OSIB"
    description = "Represent an airline flight number."

    elements = [
        TextInput(label="Airline", icon="plane"),
        TextInput(label="Flight", icon="hash"),
        TextInput(label="Date", icon="calendar"),
    ]

