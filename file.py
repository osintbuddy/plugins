import osintbuddy as ob
from osintbuddy.elements import UploadFileInput, TextInput


class File(ob.Plugin):
    label = "File"
    color = "#9CA3AF99"
    icon = "file"
    author = "OSIB"
    description = "Attach a generic file and metadata."

    elements = [
        UploadFileInput(label="Attachment", icon="file"),
        TextInput(label="Description", icon="file-description"),
    ]

