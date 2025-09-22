import osintbuddy as ob
from osintbuddy.elements import TextInput


class Gang(ob.Plugin):
    label = "Gang"
    color = "#F43F5E99"
    icon = "users-group"
    author = "OSIB"
    description = "Represent a gang or criminal group."

    elements = [
        TextInput(label="Name", icon="users-group"),
        TextInput(label="Territory", icon="map"),
    ]

