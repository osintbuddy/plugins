import osintbuddy as ob
from osintbuddy.elements import TextInput


class Female(ob.Plugin):
    version = "1.0.0"
    label = "Female"
    category = "Identity"
    color = "#EC489999"
    icon = "gender-female"
    author = "OSIB"
    description = "Represent a female person."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Age", icon="calendar"),
    ]

