from osintbuddy import Plugin
from osintbuddy.elements import TextInput


class TelegramWebsearch(Plugin):
    version = "1.0.0"
 
    label = "Telegram Websearch"
    author = "OSIB"
    description = "Web search for telegram communities"

    color = "#2AABEEaa"
    icon = "brand-telegram"

    elements = [
        TextInput(label="Query", icon="search")
    ]

    telegram_cse_urls = [
        "https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg",
        "https://cse.google.com/cse?cx=004805129374225513871:p8lhfo0g3hg",
    ]
