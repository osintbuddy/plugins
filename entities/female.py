import osintbuddy as ob
from osintbuddy.elements import TextInput


class Female(ob.Plugin):
    label = "Female"
    color = "#EC489999"
    icon = "gender-female"
    author = "OSIB"
    description = "Represent a female person."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Age", icon="calendar"),
    ]

