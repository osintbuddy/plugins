import json
from osintbuddy import Plugin
from osintbuddy.elements import TextInput, DropdownInput

try:
    import requests
    resp = requests.get('https://gist.githubusercontent.com/jerlendds/741d110f59a7d2ed2098325d30b00569/raw/25c15621eb67845db4ad65fc4ea8d3ad0991356f/cses.json')
    cses_db = json.loads(resp.text)
except Exception as e:
    print(e)
    cses_db = []


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
