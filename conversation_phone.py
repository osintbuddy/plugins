import osintbuddy as ob
from osintbuddy.elements import TextInput


class ConversationPhone(ob.Plugin):
    label = "Conversation Phone"
    color = "#06B6D499"
    icon = "phone"
    author = "OSIB"
    description = "Represent a phone conversation record."

    elements = [
        TextInput(label="Caller", icon="phone"),
        TextInput(label="Callee", icon="phone"),
        TextInput(label="Time", icon="clock"),
    ]

