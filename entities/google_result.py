from osintbuddy import Plugin
from osintbuddy.elements import Title, CopyText


class GoogleResult(Plugin):
    label = "Google Result"
    is_available = False
    color = "#3D78D999"
    elements = [Title(label="result"), CopyText(label="url")]
    icon = "brand-google"
    author = "OSIB"
