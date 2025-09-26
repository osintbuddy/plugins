import osintbuddy as ob
from osintbuddy.elements import TextInput


class MailServer(ob.Plugin):
    label = "Mail Server"
    color = "#DB277799"
    icon = "mail"
    author = "OSIB"
    description = "Represent an email (MX) server."

    elements = [
        TextInput(label="MX Host", icon="mail"),
        TextInput(label="Priority", icon="sort-ascending"),
    ]

