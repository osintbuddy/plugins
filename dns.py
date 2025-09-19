import json
import re
from osintbuddy.elements import TextInput, DropdownInput
import osintbuddy as ob



class DNS(ob.Plugin):
    label = "DNS"
    color = "#88304E99"
    icon = "creative-commons-nd"
    description = "The Domain Name System translates domains into IPs"
    elements = [
        TextInput(label="Value", icon="file-description"),
        DropdownInput(label="Record Type", options=[
            { "label": "NS" },
            { "label": "A" },
            { "label": "AAAA" },
            { "label": "CNAME" },
            { "label": "MX" },
            { "label": "SOA" },
            { "label": "TXT" },
            { "label": "PTR" },
            { "label": "SRV" },
            { "label": "CERT" },
            { "label": "DCHID" },
            { "label": "DNAME" }
        ])
    ]

    _items = [
        "NS",
        "A",
        "AAAA",
        "CNAME",
        "MX",
        "SOA",
        "TXT",
        "PTR",
        "SRV",
        "CERT",
        "DCHID",
        "DNAME",
    ]

    author = ["OSIB", "Bugfest"]

    @classmethod
    def data_template(cls):
        return {k: None for k in cls._items}

    @staticmethod
    def record(key, data):
        _data = json.dumps(data).strip("'\" .")
        match key:
            case "MX":
                matches = re.findall(r"\d+ (.*)", _data)
                _data = matches[0] if len(matches) else _data
            case "TXT":
                _data = _data.strip('\\"')

        return {
            "title": None,
            "subtitle":  f"{key} Record",
            "text": _data,
        }

    @ob.transform(label="Extract IP", icon="microscope")
    async def transform_extract_ip(self, entity) -> list:
        data = entity.value
        ip_regexp = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        results = []
        IPAddressPlugin = await ob.Registry.get_plugin('ip')
        for ip in ip_regexp.findall(data):
            blueprint = IPAddressPlugin.create(ip_address=ip)
            results.append(blueprint)
        return results


