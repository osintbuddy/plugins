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

def data_template():
    return {k: None for k in _items}

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


