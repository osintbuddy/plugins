# OSINTBuddy Plugins: Reloaded

> _I have no data yet. It is a capital mistake to theorize before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts._

---

The official default plugin collection for [OSINTBuddy](https://github.com/osintbuddy/osintbuddy). A graph-based, local-first OSINT platform for recon, link analysis, and open-source investigations.

This repository contains the default **entities** (node types) and **transforms** (graph/data operations) that ship with OSINTBuddy. It is built on top of the [`osintbuddy`](https://pypi.org/project/osintbuddy/) [framework](https://github.com/osintbuddy/framework) package.

> **Status:** Experimental. Entity definitions and transform signatures may change suddenly and without warning.

---

## What is OSINTBuddy?

An almost incomprehensible amount of data is created every day. OSINT is a method of working with, assessing, and ranking that information but the sheer volume and lack of structure leaves us drowning. OSINTBuddy Reloaded is an open-source, desktop app designed to help you cut through the noise with a graph-based interface that turns data relationships into clear visualizations, and a plugin system that lets you pull from any data source you can imagine.

The core ideas:

- **Visual intelligence:** complex data relationships rendered as interactive graphs
- **Extensible plugins:** define your own entities and transforms in Python
- **Local-first:** your data stays under your control, no cloud dependencies required outside of whatever you choose to do with plugins

---

## Concepts

### Entities

Entities are the **nodes** in the graph. Each entity type is a Python class that defines:

- What the node represents (person, IP address, domain, etc.)
- What fields it holds and how they're displayed
- Metadata like icon, color, and category

### Transforms

Transforms are **operations on entities** that produce new entities (edges in the graph). They appear in the right-click context menu on any node. A transform might:

- Resolve a domain to its IP addresses
- Look up WHOIS data for a domain
- Extract the domain from an email address
- Search for a username across platforms

### The Framework

Both entities and transforms are built with the `osintbuddy` framework package. See the [framework README](https://github.com/osintbuddy/framework/blob/main/README.md) and its [docs/](https://github.com/osintbuddy/framework/blob/main/docs/getting-started.md) for the full API reference.

---

## Available Entities

Entities are organized by category. The full list lives in [`entities/`](entities/).

### Identity

| Entity                | Description                                    |
| --------------------- | ---------------------------------------------- |
| Bad Guy               | A person of interest with adversarial context  |
| Child                 | A minor involved in an investigation           |
| Drug Dealer           | A person associated with drug-related activity |
| Female                | A female individual                            |
| Gang Leader           | Leader of a criminal organization              |
| Gang Member           | Member of a criminal organization              |
| Good Guy              | A person with a positive or neutral context    |
| Government Official   | A government representative or official        |
| Identification Number | A government-issued ID number                  |
| Judge                 | A judicial official                            |
| Law Officer           | A law enforcement officer                      |
| Male                  | A male individual                              |
| Military Officer      | A military personnel member                    |
| Passport Number       | A passport identification number               |
| Person Profile        | A general-purpose person profile               |

### Network

| Entity            | Description                        |
| ----------------- | ---------------------------------- |
| Autonomous System | An AS number and related BGP info  |
| DNS               | DNS record set for a domain        |
| IP                | An IPv4 or IPv6 address            |
| IP Geolocation    | Geolocation data for an IP address |
| MAC Address       | A hardware MAC address             |
| Mail Server       | An email mail server (MX)          |
| Name Server       | A DNS name server (NS)             |
| Ports             | Open ports on a host               |

### Web

| Entity                   | Description                                |
| ------------------------ | ------------------------------------------ |
| Certificate Transparency | A CT log certificate record                |
| Cloud Bucket             | A cloud storage bucket (S3, GCS, etc.)     |
| Darkweb Service          | A Tor hidden service or darkweb resource   |
| Favicon Hash             | A website favicon hash (Shodan-compatible) |
| HTTP Headers             | HTTP response headers                      |
| JavaScript               | JavaScript file or snippet                 |
| Onion Service            | A `.onion` hidden service                  |
| robots.txt               | A website's robots.txt                     |
| SSL Certificate          | An SSL/TLS certificate                     |
| Subdomain                | A subdomain of a domain                    |
| Tracking Codes           | Analytics/tracking identifiers             |
| URL                      | A full URL                                 |
| Website                  | A web domain/host                          |
| Whois                    | WHOIS registration data                    |

### Search

| Entity              | Description                          |
| ------------------- | ------------------------------------ |
| CSE Result          | A Google Custom Search Engine result |
| CSE Search          | A Google CSE search query            |
| Google Result       | A standard Google search result      |
| Google Search       | A Google search query                |
| Shodan              | A Shodan search or result            |
| Telegram CSE Search | A Telegram-targeted CSE search       |

### Organizations

| Entity                | Description                      |
| --------------------- | -------------------------------- |
| Church                | A religious institution          |
| Company               | A corporate entity               |
| Education Institution | A school, college, or university |
| Gang                  | A criminal organization          |
| Organization          | A general organization           |
| Political Movement    | A political party or movement    |
| Religious Group       | A religious organization         |
| Shop                  | A retail or commercial business  |

### Locations

| Entity  | Description             |
| ------- | ----------------------- |
| City    | A city                  |
| Country | A country               |
| Home    | A residential address   |
| Office  | A business address      |
| Prison  | A correctional facility |
| Region  | A geographic region     |

### Cryptocurrency

| Entity           | Description                |
| ---------------- | -------------------------- |
| Bitcoin Address  | A Bitcoin wallet address   |
| Ethereum Address | An Ethereum wallet address |
| Monero Address   | A Monero wallet address    |
| NFT Asset        | A non-fungible token asset |

### Devices

| Entity           | Description                |
| ---------------- | -------------------------- |
| Computer         | A generic computing device |
| Desktop Computer | A desktop PC               |
| Device           | A generic device           |
| Mobile Computer  | A laptop or tablet         |
| Mobile Phone     | A mobile phone             |
| Smartphone       | A smartphone               |

### Transportation

| Entity               | Description                     |
| -------------------- | ------------------------------- |
| Bike                 | A bicycle                       |
| Boat                 | A watercraft                    |
| Bus                  | A bus or coach                  |
| Car                  | An automobile                   |
| Flight Number        | An airline flight               |
| Plane                | An aircraft                     |
| Train                | A railway train                 |
| Transport            | A generic transport entity      |
| Vehicle Registration | A vehicle registration plate    |
| VIN Number           | A vehicle identification number |

### Weapons

| Entity          | Description                    |
| --------------- | ------------------------------ |
| Ammunition      | Ammunition or rounds           |
| Blade           | A bladed weapon                |
| Chemical Weapon | A chemical/biological weapon   |
| Explosive       | An explosive device component  |
| Gun             | A firearm                      |
| IED             | An improvised explosive device |
| Missile         | A guided missile               |
| Weapon          | A generic weapon               |

### Documents

| Entity        | Description                         |
| ------------- | ----------------------------------- |
| DOI           | A digital object identifier         |
| File          | A file reference                    |
| Metadata EXIF | EXIF metadata from an image or file |
| PDF Uploads   | A PDF document                      |
| PGP Key       | A PGP public or private key         |

### Communications

| Entity             | Description                  |
| ------------------ | ---------------------------- |
| Conversation       | A generic conversation       |
| Conversation Email | An email conversation thread |
| Conversation Phone | A phone call or SMS record   |

### Events

| Entity           | Description                     |
| ---------------- | ------------------------------- |
| Event            | A generic event                 |
| Incident         | A security or criminal incident |
| Meeting          | A generic meeting               |
| Meeting Business | A business meeting              |
| Meeting Social   | A social gathering              |

### Threat Intelligence

| Entity         | Description                |
| -------------- | -------------------------- |
| IOC Indicator  | An indicator of compromise |
| Malware Sample | A malware binary or sample |
| Breach Data    | Data from a known breach   |

### Other

| Entity             | Description                                 |
| ------------------ | ------------------------------------------- |
| Airport            | An airport                                  |
| Bank Account       | A bank account                              |
| Business Leader    | A business executive                        |
| Business Man       | A businessperson                            |
| Company Profile    | Extended company profile data               |
| Crime Scene        | A crime scene location                      |
| Crypto Transaction | A blockchain transaction                    |
| DeFi Contract      | A DeFi smart contract                       |
| Email Address      | An email address                            |
| File Hash          | A file hash (MD5/SHA1/SHA256)               |
| Harbor             | A maritime harbor or port                   |
| Online Group       | An online community or forum                |
| Person Profile     | A generic person profile                    |
| Phone Number       | A phone number                              |
| Train Station      | A railway station                           |
| Transport Hub      | An airport, station, or terminal            |
| Unknown            | A placeholder for unclassified data         |
| Username           | A username or handle                        |
| Username Profile   | A resolved username profile from a platform |

---

## Available Transforms

Transforms live in [`transforms/`](transforms/). The default collection covers:

| Transform file             | Target entity       | Operations                                       |
| -------------------------- | ------------------- | ------------------------------------------------ |
| `cse_result_to_url.py`     | CSE Result          | Extract the URL as a URL entity                  |
| `cse_search_to_results.py` | CSE Search          | Run a Google CSE query, return results           |
| `dns.py`                   | Domain/Website      | Resolve DNS records (A, AAAA, MX, NS, TXT, etc.) |
| `google_result.py`         | Google Result       | Convert a result to a Website entity             |
| `google_search.py`         | Google Search       | Execute a Google search, return results          |
| `ip.py`                    | IP                  | Reverse-resolve hostname, fetch geolocation      |
| `telegram_cse_search.py`   | Telegram CSE Search | Run a Telegram-targeted CSE search               |
| `url_to_website.py`        | URL / Website       | Extract the domain as a Website entity           |
| `username_profile.py`      | Username Profile    | Extract the profile link as a URL entity         |
| `username.py`              | Username            | Check username across platforms                  |
| `website_transforms.py`    | Website             | WHOIS lookup, screenshot, metadata extraction    |

---

## Expected Project Structure

Once you're ready to create plugins and transforms for the community plugins registry there's a few things to be aware of. To get started we're going to need install the [`osintbuddy`](https://pypi.org/project/osintbuddy/) package from PyPi:

```bash
python3 -m venv venv
source venv/bin/activate
pip install osintbuddy[all]
```

### 0. Build Plugins

You can find additional docs on building plugins [here!](https://github.com/osintbuddy/framework/tree/main/docs)

In short, we expect 1 and or 2 of the following folders at the root of your git repo:

- `entities/`: Plugin class definitions (one per entity type)
- `transforms/`: Transform functions decorated with @transform

All together the project structure should look something like the following.

```
plugins/
├── entities/          # Entity definitions (one file per entity type)
│   ├── ip.py
│   ├── website.py
│   ├── email_address.py
│   └── ...
├── transforms/        # Transform definitions (grouped by topic)
│   ├── dns.py
│   ├── website_transforms.py
│   └── ...
├── manifest.json      # Plugin manifest (id, name, version)
└── README.md
```

Don't sweat the `manifest.json` file yet, we'll explain that next.

### 1. `ob manifest`

We expect a `manifest.json` file generated via the CLI command: `ob manifest` before we can merge your repo details into the community registry. The `ob` CLI is available in any Python `venv/` where the [osintbuddy/framework](https://github.com/osintbuddy/framework) has been installed. Running `ob manifest` will search through all your Python files (_and or data files such as JSON, CSV, etc_) in the git repo. Once we've collected enough metadata we create a `manifest.json` file for you. `manifest.json` is displayed inside the app when you're on the Marketplaces page to provide icons, descriptions, and perhaps in time, additional information as well.

### 2. `ob readme`

Second, we suggest creating a README.md file providing a brief overview of the transforms, entities, and or data files you have added. This can be done easily and automatically by running the `ob readme` command but we suggest always reviewing the output and adjusting things as needed.

---

## Using This Plugin Set

These plugins are loaded automatically by the OSINTBuddy application for standalone use and demonstration purposes. Feel free to fork and improve anything you desire, we're open to community contributions in this repo :)

---

## License

**MIT.**

See [LICENSE](LICENSE) for details.

## Links

- [OSINTBuddy Releases](https://github.com/osintbuddy/osintbuddy/releases)
- [Plugins Framework (PyPI)](https://pypi.org/project/osintbuddy/)
- [Plugins Issue Tracker](https://github.com/osintbuddy/plugins/issues)
- [Electron Issue Tracker](https://github.com/osintbuddy/osintbuddy/issues)
- [Framework Issue Tracker](https://github.com/osintbuddy/framework/issues)
