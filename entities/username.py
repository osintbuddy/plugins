from osintbuddy.elements import TextInput
from osintbuddy import Plugin


class Username(Plugin):
    label = "Username"
    color = "#BF288D99"
    elements = [
        TextInput(label="Username", icon="user-search"),
    ]
    icon = "user-search"
    author = ["OSIB", "Artemii"]
    description = "Investigate usernames used as identification"
