import osintbuddy as ob
from osintbuddy.elements import TextInput


class ConversationEmail(ob.Plugin):
    label = "Conversation Email"
    color = "#A78BFA99"
    icon = "mail"
    author = "OSIB"
    description = "Represent an email thread or subject."

    elements = [
        TextInput(label="Subject", icon="mail"),
        TextInput(label="From", icon="at"),
        TextInput(label="To", icon="at"),
    ]

