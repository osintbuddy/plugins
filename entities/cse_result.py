from osintbuddy.elements import Title, CopyText, Text
from osintbuddy import Plugin


class CSESearchResult(Plugin):
    version = "1.0.0"

    label = "CSE Result"
    color = "#59A12866"
    icon = "brand-google"
    author = "OSIB"
    show_option = False
    
    elements = [
        Title(label="title"),
        Text(label="breadcrumb"),
        Text(label="content"),
        CopyText(label="URL"),
    ]
