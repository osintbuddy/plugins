import osintbuddy as ob
from osintbuddy.elements import TextInput


class MoneroAddress(ob.Plugin):
    version = "1.0.0"
    label = "Monero Address"
    category = "Cryptocurrency"
    color = "#FB923C99"
    icon = "currency"
    author = "OSIB"
    description = "Represent a Monero (XMR) address."

    elements = [
        TextInput(label="XMR Address", icon="currency"),
    ]

