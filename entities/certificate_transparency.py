import osintbuddy as ob
from osintbuddy.elements import TextInput


class CertificateTransparency(ob.Plugin):
    version = "1.0.0"
    label = "Certificate Transparency"
    category = "Web"
    color = "#14B8A699"
    icon = "shield-check"
    author = "OSIB"
    description = "Represent a CT log entry or lookup."

    elements = [
        TextInput(label="Domain", icon="world-www"),
        TextInput(label="Log ID", icon="shield-check"),
    ]

