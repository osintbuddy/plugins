import osintbuddy as ob
from osintbuddy.elements import TextInput


class Shop(ob.Plugin):
    version = "1.0.0"
    label = "Shop"
    color = "#FDE04799"
    icon = "building-store"
    author = "OSIB"
    description = "Represent a shop or retail location."

    elements = [
        TextInput(label="Name", icon="building-store"),
        TextInput(label="Address", icon="home"),
        TextInput(label="City", icon="building"),
    ]

