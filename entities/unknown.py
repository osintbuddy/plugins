import osintbuddy as ob
from osintbuddy.elements import TextAreaInput


class Unknown(ob.Plugin):
    version = "1.0.0"
    label = "Unknown"
    color = "#D1D5DB99"
    icon = "question-mark"
    author = "OSIB"
    description = "Placeholder for unknown/unspecified entities."

    elements = [
        TextAreaInput(label="Notes", icon="notes"),
    ]

