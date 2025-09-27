import osintbuddy as ob
from osintbuddy.elements import TextInput


class Home(ob.Plugin):
    version = "1.0.0"
    label = "Home"
    color = "#FDE04799"
    icon = "home"
    author = "OSIB"
    description = "Represent a residence address."

    elements = [
        TextInput(label="Address", icon="home"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

