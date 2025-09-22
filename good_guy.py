import osintbuddy as ob
from osintbuddy.elements import TextInput


class GoodGuy(ob.Plugin):
    label = "Good Guy"
    color = "#22C55E99"
    icon = "user-plus"
    author = "OSIB"
    description = "Represent an ally or friendly individual."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Affiliation", icon="users"),
        TextInput(label="Role", icon="id"),
    ]

