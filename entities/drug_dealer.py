import osintbuddy as ob
from osintbuddy.elements import TextInput


class DrugDealer(ob.Plugin):
    version = "1.0.0"
    label = "Drug Dealer"
    color = "#F43F5E99"
    icon = "user-minus"
    author = "OSIB"
    description = "Represent a suspected drug dealer."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Alias", icon="mask"),
        TextInput(label="Territory", icon="map"),
    ]

