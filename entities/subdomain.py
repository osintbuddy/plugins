from osintbuddy.elements import TextInput
import osintbuddy as ob


class Subdomain(ob.Plugin):
    version = "1.0.0"
    label = "Subdomain"
    is_available = True
    description = "A domain that is a part of another domain"
    color = "#093FB499"
    elements = [
        TextInput(label="Subdomain", icon="world"),
    ]
    icon = "submarine"
    author = 'OSIB'
