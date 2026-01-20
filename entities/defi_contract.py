import osintbuddy as ob
from osintbuddy.elements import TextInput


class DeFiContract(ob.Plugin):
    version = "1.0.0"
    label = "DeFi Contract"
    category = "Cryptocurrency"
    color = "#8B5CF699"
    icon = "brand-ethereum"
    author = "OSIB"
    description = "Represent a smart contract (address/network)."

    elements = [
        TextInput(label="Contract Address", icon="hash"),
        TextInput(label="Network", icon="network"),
    ]
