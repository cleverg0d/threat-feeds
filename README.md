# 🛡️ Threat Feeds by @cleverg0d

A curated collection of **free threat intelligence feeds** aggregated daily from public sources for use in:

- 🔥 FortiGate NGFW (`External Block List`)
- 📊 SIEM/SOC platforms (Wazuh, Splunk, QRadar, etc.)
- 🧪 Red/Blue team operations
- 🕵️ OSINT investigations

---

## 📦 Feeds Available

| Type    | URL                                                                 |
|---------|----------------------------------------------------------------------|
| IPs     | [feeds/ip.txt](https://raw.githubusercontent.com/cleverg0d/threat-feeds/main/feeds/ip.txt)         |
| Domains | [feeds/domain.txt](https://raw.githubusercontent.com/cleverg0d/threat-feeds/main/feeds/domain.txt) |
| URLs    | [feeds/url.txt](https://raw.githubusercontent.com/cleverg0d/threat-feeds/main/feeds/url.txt)       |

---

## ⚙️ Automation

- 🔄 Updates **daily** via GitHub Actions
- 🔁 Sources listed in `sources.json`
- 🐍 Python script: [`scripts/aggregator.py`](scripts/aggregator.py)

### 📊 Metadata

The `feeds/metadata.json` file contains information about the relevance and number of records for each type:

```json
{
  "updated_at": "2025-06-17T10:40:00Z",
  "counts": {
    "ip.txt": 4976,
    "domain.txt": 9064,
    "url.txt": 123456
  }
}
```

---

## 📚 Included Sources

- AlienVault OTX
- Abuse.ch (ThreatFox, URLHaus)
- FireHOL blocklists
- Phishing.Database (mitchellkrogza)
- Maltrail (stamparm)
- ...and other GitHub-based threat sources

---

## 🚀 Use with FortiGate NGFW

```bash
config firewall address
    edit "blocklist-IPs"
    set type external
    set fqdn "https://raw.githubusercontent.com/cleverg0d/threat-feeds/main/feeds/ip.txt"
    set external enable
next
```

---

## 🧩 Contributions

Pull requests are welcome — feel free to suggest new feeds or improvements.

---
© 2025 [cleverg0d](https://github.com/cleverg0d) • Open Threat Intelligence Initiative