import osintbuddy as ob
from osintbuddy.elements import TextInput


class CryptoTransaction(ob.Plugin):
    label = "Crypto Transaction"
    color = "#F59E0B99"
    icon = "currency"
    author = "OSIB"
    description = "Represent a blockchain transaction (hash/network)."

    elements = [
        TextInput(label="Tx Hash", icon="hash"),
        TextInput(label="Network", icon="network"),
    ]
