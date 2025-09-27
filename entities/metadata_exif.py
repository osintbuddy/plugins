import osintbuddy as ob
from osintbuddy.elements import UploadFileInput, TextInput


class MetadataEXIF(ob.Plugin):
    version = "1.0.0"
    label = "Metadata EXIF"
    color = "#94A3B899"
    icon = "photo"
    author = "OSIB"
    description = "Attach an image and record parsed EXIF fields."

    elements = [
        UploadFileInput(label="Image", icon="photo", accept="image/*"),
        TextInput(label="Camera", icon="camera"),
        TextInput(label="Timestamp", icon="calendar"),
        TextInput(label="GPS", icon="map-pin"),
    ]
