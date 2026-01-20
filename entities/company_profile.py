import osintbuddy as ob
from osintbuddy.elements import TextInput


class CompanyProfile(ob.Plugin):
    version = "1.0.0"
    label = "Company Profile"
    category = "Organizations"
    color = "#F59E0B99"
    icon = "building"
    author = "OSIB"
    description = "Store basic company/organization details."

    elements = [
        TextInput(label="Company", icon="building"),
        TextInput(label="Domain", icon="world-www"),
        TextInput(label="Country", icon="flag"),
    ]

