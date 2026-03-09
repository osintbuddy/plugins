# OSIB Official: Plugins Reloaded

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

## Available Entities

| Entity                   | ID                             | Category                       | Description                                                                                                                            | File                                 |
| ------------------------ | ------------------------------ | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Airport                  | airport@1.0.0                  | Locations, Transportation      | Represent an airport (IATA/ICAO codes and name).                                                                                       | entities/airport.py                  |
| Ammunition               | ammunition@1.0.0               | Weapons                        | Represent ammunition type and caliber.                                                                                                 | entities/ammunition.py               |
| Autonomous System        | autonomous_system@1.0.0        | Network                        | Represent an Autonomous System (ASN).                                                                                                  | entities/autonomous_system.py        |
| Bad Guy                  | bad_guy@1.0.0                  | Identity                       | Represent a suspect or hostile individual.                                                                                             | entities/bad_guy.py                  |
| Bank Account             | bank_account@1.0.0             | Finance, Identity              | Represent a bank account identifier.                                                                                                   | entities/bank_account.py             |
| Bike                     | bike@1.0.0                     | Transportation                 | Represent a bicycle with make/model.                                                                                                   | entities/bike.py                     |
| Bitcoin Address          | bitcoin_address@1.0.0          | Cryptocurrency                 | Represent a Bitcoin address.                                                                                                           | entities/bitcoin_address.py          |
| Blade                    | blade@1.0.0                    | Weapons                        | Represent an edged weapon (knife/machete).                                                                                             | entities/blade.py                    |
| Boat                     | boat@1.0.0                     | Transportation                 | Represent a watercraft registration.                                                                                                   | entities/boat.py                     |
| Breach Data              | breach_data@1.0.0              | Threat Intelligence, Documents | Reference breached data sources or upload small snippets.                                                                              | entities/breach_data.py              |
| Bus                      | bus@1.0.0                      | Transportation                 | Represent a bus vehicle identifier.                                                                                                    | entities/bus.py                      |
| Business Leader          | business_leader@1.0.0          | Identity, Organizations        | Represent an executive or business leader.                                                                                             | entities/business_leader.py          |
| Business Man             | business_man@1.0.0             | Identity, Organizations        | Represent a businessman or professional.                                                                                               | entities/business_man.py             |
| Car                      | car@1.0.0                      | Transportation                 | Represent an automobile.                                                                                                               | entities/car.py                      |
| Certificate Transparency | certificate_transparency@1.0.0 | Web                            | Represent a CT log entry or lookup.                                                                                                    | entities/certificate_transparency.py |
| Chemical Weapon          | chemical_weapon@1.0.0          | Weapons                        | Represent a chemical weapon classification.                                                                                            | entities/chemical_weapon.py          |
| Child                    | child@1.0.0                    | Identity                       | Represent a child (basic demographics).                                                                                                | entities/child.py                    |
| Church                   | church@1.0.0                   | Organizations                  | Represent a church or religious building.                                                                                              | entities/church.py                   |
| City                     | city@1.0.0                     | Locations                      | Represent a city.                                                                                                                      | entities/city.py                     |
| Cloud Bucket             | cloud_bucket@1.0.0             | Web                            | Represent a cloud storage bucket (S3/GCS/Azure).                                                                                       | entities/cloud_bucket.py             |
| Company                  | company@1.0.0                  | Organizations                  | Represent a company or organization entry.                                                                                             | entities/company.py                  |
| Company Profile          | company_profile@1.0.0          | Organizations, Documents       | Store basic company/organization details.                                                                                              | entities/company_profile.py          |
| Computer                 | computer@1.0.0                 | Devices                        | Represent a computer asset.                                                                                                            | entities/computer.py                 |
| Conversation             | conversation@1.0.0             | Communications                 | Represent a conversation reference.                                                                                                    | entities/conversation.py             |
| Conversation Email       | conversation_email@1.0.0       | Communications                 | Represent an email thread or subject.                                                                                                  | entities/conversation_email.py       |
| Conversation Phone       | conversation_phone@1.0.0       | Communications                 | Represent a phone conversation record.                                                                                                 | entities/conversation_phone.py       |
| Country                  | country@1.0.0                  | Locations                      | Represent a country.                                                                                                                   | entities/country.py                  |
| Crime Scence             | crime_scence@1.0.0             | Events, Locations              | Represent a crime scene reference (location/time).                                                                                     | entities/crime_scence.py             |
| Crypto Transaction       | crypto_transaction@1.0.0       | Cryptocurrency, Finance        | Represent a blockchain transaction (hash/network).                                                                                     | entities/crypto_transaction.py       |
| Darkweb Service          | darkweb_service@1.0.0          | Web                            | Represent a darkweb/onion service reference.                                                                                           | entities/darkweb_service.py          |
| DeFi Contract            | defi_contract@1.0.0            | Cryptocurrency, Finance        | Represent a smart contract (address/network).                                                                                          | entities/defi_contract.py            |
| Desktop Computer         | desktop_computer@1.0.0         | Devices                        | Represent a desktop computer asset.                                                                                                    | entities/desktop_computer.py         |
| Device                   | device@1.0.0                   | Devices                        | Represent a generic device.                                                                                                            | entities/device.py                   |
| DNS                      | dns@1.0.0                      | Network                        | The Domain Name System translates domains into IPs                                                                                     | entities/dns.py                      |
| DOI                      | doi@1.0.0                      | Documents                      | A a digital identifier of an object, any object; physical, digital, or abstract. DOIs solve a common problem: keeping track of things. | entities/doi.py                      |
| Drug Dealer              | drug_dealer@1.0.0              | Identity                       | Represent a suspected drug dealer.                                                                                                     | entities/drug_dealer.py              |
| Education Instituion     | education_instituion@1.0.0     | Organizations                  | Represent an educational institution.                                                                                                  | entities/education_instituion.py     |
| Email Address            | email_address@1.0.0            | Identity, Communications       | Represent and store an email address.                                                                                                  | entities/email_address.py            |
| Ethereum Address         | ethereum_address@1.0.0         | Cryptocurrency                 | Represent an Ethereum address.                                                                                                         | entities/ethereum_address.py         |
| Event                    | event@1.0.0                    | Events                         | Represent an event occurrence.                                                                                                         | entities/event.py                    |
| Explosive                | explosive@1.0.0                | Weapons                        | Represent an explosive material or device.                                                                                             | entities/explosive.py                |
| Favicon Hash             | favicon_hash@1.0.0             | Web                            | Represent an HTTP favicon hash (e.g., for Shodan/Censys).                                                                              | entities/favicon_hash.py             |
| Female                   | female@1.0.0                   | Identity                       | Represent a female person.                                                                                                             | entities/female.py                   |
| File                     | file@1.0.0                     | Documents                      | Attach a generic file and metadata.                                                                                                    | entities/file.py                     |
| File Hash                | file_hash@1.0.0                | Documents, Threat Intelligence | Represent a file hash (MD5/SHA1/SHA256).                                                                                               | entities/file_hash.py                |
| Flight Number            | flight_number@1.0.0            | Transportation                 | Represent an airline flight number.                                                                                                    | entities/flight_number.py            |
| Gang                     | gang@1.0.0                     | Organizations                  | Represent a gang or criminal group.                                                                                                    | entities/gang.py                     |
| Gang Leader              | gang_leader@1.0.0              | Identity                       | Represent a gang leader.                                                                                                               | entities/gang_leader.py              |
| Gang Member              | gang_member@1.0.0              | Identity                       | Represent a gang member.                                                                                                               | entities/gang_member.py              |
| Good Guy                 | good_guy@1.0.0                 | Identity                       | Represent an ally or friendly individual.                                                                                              | entities/good_guy.py                 |
| Google Result            | google_result@1.0.0            | Search                         |                                                                                                                                        | entities/google_result.py            |
| Google Search            | google_search@1.0.0            | Search                         | Search google using the advanced operators you're used to                                                                              | entities/google_search.py            |
| Government Official      | government_official@1.0.0      | Identity                       | Represent a government official.                                                                                                       | entities/government_official.py      |
| Gun                      | gun@1.0.0                      | Weapons                        | Represent a firearm (make/model/serial).                                                                                               | entities/gun.py                      |
| Harbor                   | harbor@1.0.0                   | Locations, Transportation      | Represent a harbor or port location.                                                                                                   | entities/harbor.py                   |
| Home                     | home@1.0.0                     | Locations                      | Represent a residence address.                                                                                                         | entities/home.py                     |
| HTTP Headers             | http_headers@1.0.0             | Web                            | Represent HTTP response headers for a URL.                                                                                             | entities/http_headers.py             |
| Identification Number    | identification_number@1.0.0    | Identity                       | Represent a government-issued ID number.                                                                                               | entities/identification_number.py    |
| IED                      | ied@1.0.0                      | Weapons                        | Represent an improvised explosive device.                                                                                              | entities/ied.py                      |
| Incident                 | incident@1.0.0                 | Events                         | Represent a security or criminal incident.                                                                                             | entities/incident.py                 |
| IOC Indicator            | ioc_indicator@1.0.0            | Threat Intelligence            | Represent an Indicator of Compromise (type/value).                                                                                     | entities/ioc_indicator.py            |
| IP                       | ip@1.0.0                       | Network                        | Internet Protocol address                                                                                                              | entities/ip.py                       |
| IP Geolocation           | ip_geolocation@1.0.0           | Network, Locations             |                                                                                                                                        | entities/ip_geolocation.py           |
| JavaScript               | javascript@1.0.0               | Web                            | Represent a JavaScript resource reference.                                                                                             | entities/javascript.py               |
| Judge                    | judge@1.0.0                    | Identity                       | Represent a judge.                                                                                                                     | entities/judge.py                    |
| Law Officer              | law_officer@1.0.0              | Identity                       | Represent a law enforcement officer.                                                                                                   | entities/law_officer.py              |
| MAC Address              | mac_address@1.0.0              | Network                        | Represent a device MAC address.                                                                                                        | entities/mac_address.py              |
| Mail Server              | mail_server@1.0.0              | Network                        | Represent an email (MX) server.                                                                                                        | entities/mail_server.py              |
| Male                     | male@1.0.0                     | Identity                       | Represent a male person.                                                                                                               | entities/male.py                     |
| Malware Sample           | malware_sample@1.0.0           | Threat Intelligence, Documents | Store a malware sample (handle with care).                                                                                             | entities/malware_sample.py           |
| Meeting                  | meeting@1.0.0                  | Events                         | Represent a generic meeting.                                                                                                           | entities/meeting.py                  |
| Meeting Business         | meeting_business@1.0.0         | Events                         | Represent a business meeting.                                                                                                          | entities/meeting_business.py         |
| Meeting Social           | meeting_social@1.0.0           | Events                         | Represent a social meeting or gathering.                                                                                               | entities/meeting_social.py           |
| Metadata EXIF            | metadata_exif@1.0.0            | Documents                      | Attach an image and record parsed EXIF fields.                                                                                         | entities/metadata_exif.py            |
| Military Officer         | military_officer@1.0.0         | Identity                       | Represent a military officer.                                                                                                          | entities/military_officer.py         |
| Missile                  | missile@1.0.0                  | Weapons                        | Represent a missile system.                                                                                                            | entities/missile.py                  |
| Mobile Computer          | mobile_computer@1.0.0          | Devices                        | Represent a laptop or tablet.                                                                                                          | entities/mobile_computer.py          |
| Mobile Phone             | mobile_phone@1.0.0             | Devices                        | Represent a mobile handset.                                                                                                            | entities/mobile_phone.py             |
| Monero Address           | monero_address@1.0.0           | Cryptocurrency                 | Represent a Monero (XMR) address.                                                                                                      | entities/monero_address.py           |
| Name Server              | name_server@1.0.0              | Network                        | Represent a DNS nameserver (NS).                                                                                                       | entities/name_server.py              |
| NFT Asset                | nft_asset@1.0.0                | Cryptocurrency                 | Represent an NFT (contract/token ID).                                                                                                  | entities/nft_asset.py                |
| Office                   | office@1.0.0                   | Locations                      | Represent an office location.                                                                                                          | entities/office.py                   |
| Onion Service            | onion_service@1.0.0            | Web                            | Represent a Tor hidden service (v3).                                                                                                   | entities/onion_service.py            |
| Online Group             | online_group@1.0.0             | Social Media, Organizations    | Represent an online group or community.                                                                                                | entities/online_group.py             |
| Organization             | organization@1.0.0             | Organizations                  | Represent an organization entity.                                                                                                      | entities/organization.py             |
| Passport Number          | passport_number@1.0.0          | Identity                       | Represent a passport number.                                                                                                           | entities/passport_number.py          |
| PDF Uploads              | pdf_uploads@1.0.0              | Documents                      | Upload a PDF document for analysis or reference.                                                                                       | entities/pdf_file.py                 |
| Person Profile           | person_profile@1.0.0           | Identity                       | Store basic person profile details.                                                                                                    | entities/person_profile.py           |
| PGP Key                  | pgp_key@1.0.0                  | Documents                      | Represent a PGP public key reference.                                                                                                  | entities/pgp_key.py                  |
| Phone Number             | phone_number@1.0.0             | Identity, Communications       | Represent and store a phone number (E.164).                                                                                            | entities/phone_number.py             |
| Plane                    | plane@1.0.0                    | Transportation                 | Represent an aircraft.                                                                                                                 | entities/plane.py                    |
| Political Movement       | political_movement@1.0.0       | Organizations                  | Represent a political movement.                                                                                                        | entities/political_movement.py       |
| Ports                    | ports@1.0.0                    | Locations, Transportation      | Represent a service port and protocol.                                                                                                 | entities/ports.py                    |
| Prison                   | prison@1.0.0                   | Locations                      | Represent a prison or detention facility.                                                                                              | entities/prison.py                   |
| Region                   | region@1.0.0                   | Locations                      | Represent a geographic region.                                                                                                         | entities/region.py                   |
| Religious Group          | religious_group@1.0.0          | Organizations                  | Represent a religious group.                                                                                                           | entities/religious_group.py          |
| robots.txt               | robots.txt@1.0.0               | Web                            | Represent a robots.txt reference for a domain.                                                                                         | entities/robots_txt.py               |
| Shodan                   | shodan@1.0.0                   | Search                         | Represent a Shodan query or result reference.                                                                                          | entities/shodan.py                   |
| Shop                     | shop@1.0.0                     | Organizations                  | Represent a shop or retail location.                                                                                                   | entities/shop.py                     |
| Smartphone               | smartphone@1.0.0               | Devices                        | Represent a smartphone device.                                                                                                         | entities/smartphone.py               |
| SSL Certificate          | ssl_certificate@1.0.0          | Web                            | Represent details from an SSL/TLS certificate.                                                                                         | entities/ssl_certificate.py          |
| Subdomain                | subdomain@1.0.0                | Web                            | A domain that is a part of another domain                                                                                              | entities/subdomain.py                |
| Tracking Codes           | tracking_codes@1.0.0           | Web                            | Represent website analytics/ads tracking codes.                                                                                        | entities/tracking_codes.py           |
| Train                    | train@1.0.0                    | Transportation                 | Represent a train identifier.                                                                                                          | entities/train.py                    |
| Train Station            | train_station@1.0.0            | Locations, Transportation      | Represent a train station.                                                                                                             | entities/train_station.py            |
| Transport                | transport@1.0.0                | Transportation                 | Represent a transport item or reference.                                                                                               | entities/transport.py                |
| Transport Hub            | transport_hub@1.0.0            | Locations, Transportation      | Represent a transport hub (airport/station/port).                                                                                      | entities/transport_hub.py            |
| Unknown                  | unknown@1.0.0                  | Generic                        | Placeholder for unknown/unspecified entities.                                                                                          | entities/unknown.py                  |
| URL                      | url@1.0.0                      | Web                            | Uniform Resource Locator, usually starts with https://                                                                                 | entities/url.py                      |
| Username                 | username@1.0.0                 | Identity, Social Media         | Investigate usernames used as identification                                                                                           | entities/username.py                 |
| Username Profile         | username_profile@1.0.0         | Social Media, Identity         |                                                                                                                                        | entities/username_profile.py         |
| Vehicle Registration     | vehicle_registration@1.0.0     | Transportation                 | Represent a vehicle registration record.                                                                                               | entities/vehicle_registration.py     |
| VIN Number               | vin_number@1.0.0               | Transportation                 | Represent a Vehicle Identification Number.                                                                                             | entities/vin_number.py               |
| Weapon                   | weapon@1.0.0                   | Weapons                        | Represent a weapon (generic).                                                                                                          | entities/weapon.py                   |
| Website                  | website@1.0.0                  | Web                            | Represents a domain from a website on the internet                                                                                     | entities/website.py                  |
| Whois                    | whois@1.0.0                    | Web                            | whois.com allows you to trace the ownership and tenure of a domain name or an IP address                                               | entities/whois.py                    |

## Available Transforms

| Transform               | Target                 | Description             | File                             |
| ----------------------- | ---------------------- | ----------------------- | -------------------------------- |
| Extract IP              | dns@1.0.0              | Extract IP              | transforms/dns.py                |
| To website              | google_result@1.0.0    | To website              | transforms/google_result.py      |
| To results              | google_result@1.0.0    | To results              | transforms/google_search.py      |
| To geolocation          | ip@1.0.0               | To geolocation          | transforms/ip.py                 |
| To subdomains           | ip@1.0.0               | To subdomains           | transforms/ip.py                 |
| To website              | ip@1.0.0               | To website              | transforms/ip.py                 |
| To website              | website@1.0.0          | To website              | transforms/url_to_website.py     |
| To checkuser.vercel.app | username@1.0.0         | To checkuser.vercel.app | transforms/username.py           |
| To URL                  | username_profile@1.0.0 | To URL                  | transforms/username_profile.py   |
| To DNS                  | website@1.0.0          | To DNS                  | transforms/website_transforms.py |
| To google               | website@1.0.0          | To google               | transforms/website_transforms.py |
| To IP                   | website@1.0.0          | To IP                   | transforms/website_transforms.py |
| To WHOIS                | website@1.0.0          | To WHOIS                | transforms/website_transforms.py |

## Data Files

| File                          | Type | Purpose                              |
| ----------------------------- | ---- | ------------------------------------ |
| .github/workflows/release.yml | yml  | Configuration or structured metadata |

## Operational Notes

Detected external dependencies: httpx, selenium
