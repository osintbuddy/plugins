from osintbuddy.elements import CopyText, TextAreaInput, Empty
import osintbuddy as ob


class Whois(ob.Plugin):
    label = "Whois"
    is_available = False
    color = "#F47C00"
    entity = [
        [TextAreaInput(label="Whois Data")],
        [CopyText(label="raw whois data", icon="world-search"), Empty()],
    ]
    icon = "world-search"
    author = "team@OSINTBuddy"
