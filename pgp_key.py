import osintbuddy as ob
from osintbuddy.elements import TextInput


class PGPKey(ob.Plugin):
    label = "PGP Key"
    color = "#22C55E99"
    icon = "key"
    author = "OSIB"
    description = "Represent a PGP public key reference."

    elements = [
        TextInput(label="Key ID", icon="key"),
        TextInput(label="Fingerprint", icon="fingerprint"),
        TextInput(label="Email", icon="at"),
    ]
