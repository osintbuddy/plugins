from osintbuddy.elements import TextInput
import osintbuddy as ob


class Subdomain(ob.Plugin):
    label = "Subdomain"
    is_available = False
    color = "#FFCC33"
    entity = [
        TextInput(label="Subdomain", icon="world"),
    ]
    icon = "submarine"
    author = 'team@OSINTBuddy'
