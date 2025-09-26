import osintbuddy as ob
from osintbuddy.elements import TextInput


class BusinessLeader(ob.Plugin):
    label = "Business Leader"
    color = "#F59E0B99"
    icon = "briefcase"
    author = "OSIB"
    description = "Represent an executive or business leader."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Company", icon="building"),
        TextInput(label="Title", icon="id"),
    ]

