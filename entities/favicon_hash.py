import osintbuddy as ob
from osintbuddy.elements import TextInput


class FaviconHash(ob.Plugin):
    version = "1.0.0"
    label = "Favicon Hash"
    color = "#EC489999"
    icon = "brand-google-chrome"
    author = "OSIB"
    description = "Represent an HTTP favicon hash (e.g., for Shodan/Censys)."

    elements = [
        TextInput(label="MD5 Hash", icon="hash"),
        TextInput(label="URL", icon="link"),
    ]

