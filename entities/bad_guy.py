import osintbuddy as ob
from osintbuddy.elements import TextInput


class BadGuy(ob.Plugin):
    version = "1.0.0"
    label = "Bad Guy"
    color = "#EF444499"
    icon = "user-minus"
    author = "OSIB"
    description = "Represent a suspect or hostile individual."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Alias", icon="mask"),
        TextInput(label="Affiliation", icon="users"),
    ]

