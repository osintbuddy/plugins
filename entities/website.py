import socket
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from osintbuddy.elements import TextInput
from osintbuddy.errors import PluginError
import osintbuddy as ob


class Website(ob.Plugin):
    version = "1.0.0"

    label = "Website"
    description = "Represents a domain from a website on the internet"
    author = "OSIB"
    
    color = "#1D1DB899"
    icon = "world-www"
    
    elements = [
        TextInput(label="Domain", icon="world-www"),
    ]


