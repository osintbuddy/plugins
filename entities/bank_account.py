import osintbuddy as ob
from osintbuddy.elements import TextInput


class BankAccount(ob.Plugin):
    version = "1.0.0"
    label = "Bank Account"
    category = ["Finance", "Identity"]
    color = "#06B6D499"
    icon = "building-bank"
    author = "OSIB"
    description = "Represent a bank account identifier."

    elements = [
        TextInput(label="Account Number", icon="hash"),
        TextInput(label="IBAN", icon="hash"),
        TextInput(label="Bank Name", icon="building"),
    ]

