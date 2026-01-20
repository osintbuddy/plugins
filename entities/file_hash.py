import osintbuddy as ob
from osintbuddy.elements import TextInput


class FileHash(ob.Plugin):
    version = "1.0.0"
    label = "File Hash"
    category = ["Documents", "Threat Intelligence"]
    color = "#F9731699"
    icon = "hash"
    author = "OSIB"
    description = "Represent a file hash (MD5/SHA1/SHA256)."

    elements = [
        TextInput(label="Hash", icon="hash"),
        TextInput(label="Algorithm", icon="settings"),
    ]

