from osintbuddy.elements import CopyText, TextAreaInput, Empty
import osintbuddy as ob


class Whois(ob.Plugin):
    version = "1.0.0"
    label = "Whois"
    is_available = False
    color = "#F47C0099"
    elements = [
        TextAreaInput(label="Raw WHOIS"),
        [Empty(), Empty()]
    ]
    icon = "world-question"
    author = "OSIB"
    description = "whois.com allows you to trace the ownership and tenure of a domain name or an IP address"
