import osintbuddy as ob
from osintbuddy.elements import TextInput


class HTTPHeaders(ob.Plugin):
    version = "1.0.0"
    label = "HTTP Headers"
    color = "#8B5CF699"
    icon = "brackets"
    author = "OSIB"
    description = "Represent HTTP response headers for a URL."

    elements = [
        TextInput(label="URL", icon="link"),
    ]

