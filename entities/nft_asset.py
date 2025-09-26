import osintbuddy as ob
from osintbuddy.elements import TextInput


class NFTAsset(ob.Plugin):
    label = "NFT Asset"
    color = "#A855F799"
    icon = "photo-up"
    author = "OSIB"
    description = "Represent an NFT (contract/token ID)."

    elements = [
        TextInput(label="Contract", icon="hash"),
        TextInput(label="Token ID", icon="hash"),
        TextInput(label="Chain", icon="network"),
    ]
