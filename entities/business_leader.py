import osintbuddy as ob
from osintbuddy.elements import TextInput


class BusinessLeader(ob.Plugin):
    version = "1.0.0"
    label = "Business Leader"
    category = "Identity"
    color = "#F59E0B99"
    icon = "briefcase"
    author = "OSIB"
    description = "Represent an executive or business leader."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Company", icon="building"),
        TextInput(label="Title", icon="id"),
    ]

