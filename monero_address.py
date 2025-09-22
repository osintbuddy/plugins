import osintbuddy as ob
from osintbuddy.elements import TextInput


class MoneroAddress(ob.Plugin):
    label = "Monero Address"
    color = "#FB923C99"
    icon = "currency"
    author = "OSIB"
    description = "Represent a Monero (XMR) address."

    elements = [
        TextInput(label="XMR Address", icon="currency"),
    ]

