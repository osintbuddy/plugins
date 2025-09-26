import osintbuddy as ob
from osintbuddy.elements import TextInput


class EthereumAddress(ob.Plugin):
    version = "1.0.0"
    label = "Ethereum Address"
    color = "#6366F199"
    icon = "currency-ethereum"
    author = "OSIB"
    description = "Represent an Ethereum address."

    elements = [
        TextInput(label="ETH Address", icon="currency-ethereum"),
    ]

