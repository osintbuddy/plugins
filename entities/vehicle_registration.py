import osintbuddy as ob
from osintbuddy.elements import TextInput


class VehicleRegistration(ob.Plugin):
    version = "1.0.0"
    label = "Vehicle Registration"
    category = "Transportation"
    color = "#9CA3AF99"
    icon = "id"
    author = "OSIB"
    description = "Represent a vehicle registration record."

    elements = [
        TextInput(label="Plate", icon="hash"),
        TextInput(label="State/Region", icon="map"),
        TextInput(label="VIN", icon="hash"),
    ]

