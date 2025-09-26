import json
import re
from osintbuddy.elements import TextInput, DropdownInput
import osintbuddy as ob

class DOI(ob.Plugin):
    version = "1.0.0"
    label = "DOI"
    color = "#fab60899"
    icon = "object-scan"
    description = "A a digital identifier of an object, any object; physical, digital, or abstract. DOIs solve a common problem: keeping track of things."
    elements = [
        TextInput(label="DOI", icon="file-description"),
    ]