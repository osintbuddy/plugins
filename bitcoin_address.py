import osintbuddy as ob
from osintbuddy.elements import TextInput


class BitcoinAddress(ob.Plugin):
    label = "Bitcoin Address"
    color = "#F59E0B99"
    icon = "currency-bitcoin"
    author = "OSIB"
    description = "Represent a Bitcoin address."

    elements = [
        TextInput(label="BTC Address", icon="currency-bitcoin"),
    ]

