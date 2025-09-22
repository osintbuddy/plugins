import osintbuddy as ob
from osintbuddy.elements import TextInput


class EducationInstituion(ob.Plugin):
    label = "Education Instituion"
    color = "#A78BFA99"
    icon = "school"
    author = "OSIB"
    description = "Represent an educational institution."

    elements = [
        TextInput(label="Name", icon="school"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

