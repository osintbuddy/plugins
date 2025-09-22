import osintbuddy as ob
from osintbuddy.elements import TextInput


class BankAccount(ob.Plugin):
    label = "Bank Account"
    color = "#06B6D499"
    icon = "building-bank"
    author = "OSIB"
    description = "Represent a bank account identifier."

    elements = [
        TextInput(label="Account Number", icon="hash"),
        TextInput(label="IBAN", icon="hash"),
        TextInput(label="Bank Name", icon="building"),
    ]

