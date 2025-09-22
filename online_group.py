import osintbuddy as ob
from osintbuddy.elements import TextInput


class OnlineGroup(ob.Plugin):
    label = "Online Group"
    color = "#A78BFA99"
    icon = "users"
    author = "OSIB"
    description = "Represent an online group or community."

    elements = [
        TextInput(label="Platform", icon="world-www"),
        TextInput(label="Group Name", icon="users"),
        TextInput(label="URL", icon="link"),
    ]

