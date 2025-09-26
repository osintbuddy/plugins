import osintbuddy as ob
from osintbuddy.elements import TextInput


class Unknown(ob.Plugin):
    label = "Unknown"
    color = "#D1D5DB99"
    icon = "question-mark"
    author = "OSIB"
    description = "Placeholder for unknown/unspecified entities."

    elements = [
        TextInput(label="Notes", icon="notes"),
    ]

