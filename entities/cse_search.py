from osintbuddy import Plugin, read_resource_json
from osintbuddy.elements import TextInput, DropdownInput


cses_db = read_resource_json(__file__, "cses.json", default=[])

class GoogleCSESearch(Plugin):
    version = "1.0.0"

    label = "CSE Search"
    description = 'Search through hundreds of categorized custom search engines from Google'
    author = "OSIB"

    color = "#78C84166"
    icon = "world-search"

    elements = [
        [
            TextInput(label="Query", icon="search"),
            DropdownInput(label="Max Results", value={"label": "100"}, options=[
                { "label": "10" },
                { "label": "20" },
                { "label": "30" },
                { "label": "40" },
                { "label": "50" },
                { "label": "60" },
                { "label": "70" },
                { "label": "80" },
                { "label": "90" },
                { "label": "100" }
            ]),
        ],
        DropdownInput(label="CSE Categories", options=cses_db)
    ]
