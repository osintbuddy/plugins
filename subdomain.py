from osintbuddy.elements import TextInput
import osintbuddy as ob


class Subdomain(ob.Plugin):
    label = "Subdomain"
    is_available = True
    description = "A domain that is a part of another domain"
    color = "#272ebe"
    entity = [
        TextInput(label="Subdomain", icon="world"),
    ]
    icon = "submarine"
    author = 'OSIB'
