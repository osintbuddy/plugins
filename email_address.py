import osintbuddy as ob
from osintbuddy.elements import TextInput


class EmailAddress(ob.Plugin):
    label = "Email Address"
    color = "#0D948899"
    icon = "at"
    author = "OSIB"
    description = "Represent and store an email address."

    elements = [
        TextInput(label="Email", icon="at"),
    ]

