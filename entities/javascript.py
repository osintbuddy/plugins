import osintbuddy as ob
from osintbuddy.elements import TextInput


class JavaScript(ob.Plugin):
    version = "1.0.0"
    label = "JavaScript"
    color = "#EAB30899"
    icon = "brand-javascript"
    author = "OSIB"
    description = "Represent a JavaScript resource reference."

    elements = [
        TextInput(label="URL", icon="link"),
        TextInput(label="Hash", icon="hash"),
    ]
