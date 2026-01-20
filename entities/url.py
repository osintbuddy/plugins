from urllib.parse import urlparse
from osintbuddy.elements import TextInput
from osintbuddy import Plugin



class URL(Plugin):
    version = "1.0.0"

    label = 'URL'
    category = "Web"
    author = 'OSIB'
    description = 'Uniform Resource Locator, usually starts with https://'

    color = '#47139699'
    elements = [
        TextInput(label="URL", icon="link"),
    ]
