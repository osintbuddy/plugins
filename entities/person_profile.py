import osintbuddy as ob
from osintbuddy.elements import TextInput


class PersonProfile(ob.Plugin):
    label = "Person Profile"
    color = "#6366F199"
    icon = "user"
    author = "OSIB"
    description = "Store basic person profile details."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Username", icon="user-search"),
        TextInput(label="Location", icon="map"),
    ]

