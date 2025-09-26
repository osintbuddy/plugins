import osintbuddy as ob
from osintbuddy.elements import TextInput


class Conversation(ob.Plugin):
    label = "Conversation"
    color = "#34D39999"
    icon = "messages"
    author = "OSIB"
    description = "Represent a conversation reference."

    elements = [
        TextInput(label="Channel", icon="message"),
        TextInput(label="Participants", icon="users"),
    ]

