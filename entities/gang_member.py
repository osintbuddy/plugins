import osintbuddy as ob
from osintbuddy.elements import TextInput


class GangMember(ob.Plugin):
    label = "Gang Member"
    color = "#FB718599"
    icon = "user"
    author = "OSIB"
    description = "Represent a gang member."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Gang", icon="users-group"),
        TextInput(label="Alias", icon="mask"),
    ]

