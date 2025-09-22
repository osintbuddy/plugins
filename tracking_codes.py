import osintbuddy as ob
from osintbuddy.elements import TextInput


class TrackingCodes(ob.Plugin):
    label = "Tracking Codes"
    color = "#06B6D499"
    icon = "scan"
    author = "OSIB"
    description = "Represent website analytics/ads tracking codes."

    elements = [
        TextInput(label="Google Analytics", icon="brand-google-analytics"),
        TextInput(label="Google Tag Manager", icon="barcode"),
        TextInput(label="Facebook Pixel", icon="brand-facebook"),
    ]
