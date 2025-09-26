import osintbuddy as ob
from osintbuddy.elements import TextInput


class HTTPHeaders(ob.Plugin):
    label = "HTTP Headers"
    color = "#8B5CF699"
    icon = "brackets"
    author = "OSIB"
    description = "Represent HTTP response headers for a URL."

    elements = [
        TextInput(label="URL", icon="link"),
    ]

