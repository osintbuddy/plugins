import osintbuddy as ob
from osintbuddy.elements import TextInput


class GangLeader(ob.Plugin):
    version = "1.0.0"
    label = "Gang Leader"
    color = "#EF444499"
    icon = "user-star"
    author = "OSIB"
    description = "Represent a gang leader."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Gang", icon="users-group"),
        TextInput(label="Alias", icon="mask"),
    ]

