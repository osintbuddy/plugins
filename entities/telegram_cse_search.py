from osintbuddy import Plugin
from osintbuddy.elements import TextInput


class TelegramWebsearch(Plugin):
    version = "1.0.0"
 
    label = "Telegram CSE Search"
    author = "OSIB"
    description = "CSE search for telegram communities"

    color = "#2AABEEaa"
    icon = "brand-telegram"

    elements = [
        TextInput(label="Query", icon="search")
    ]
