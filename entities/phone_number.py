import osintbuddy as ob
from osintbuddy.elements import TextInput


class PhoneNumber(ob.Plugin):
    label = "Phone Number"
    color = "#10B98199"
    icon = "phone"
    author = "OSIB"
    description = "Represent and store a phone number (E.164)."

    elements = [
        TextInput(label="Phone", icon="phone"),
    ]

