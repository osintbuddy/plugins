import osintbuddy as ob
from osintbuddy.elements import TextInput


class CompanyProfile(ob.Plugin):
    label = "Company Profile"
    color = "#F59E0B99"
    icon = "building"
    author = "OSIB"
    description = "Store basic company/organization details."

    elements = [
        TextInput(label="Company", icon="building"),
        TextInput(label="Domain", icon="world-www"),
        TextInput(label="Country", icon="flag"),
    ]

