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

You can integrate these threat feeds directly into **FortiGate firewalls** using the built-in *Threat Feed* connector.

### 🧩 Supported Feed Types and URLs

| Type   | GitHub Raw URL |
|--------|----------------|
| IP     | `https://raw.githubusercontent.com/cleverg0d/threat-feeds/main/feeds/ip.txt` |
| Domain | `https://raw.githubusercontent.com/cleverg0d/threat-feeds/main/feeds/domain.txt` |
| URL    | `https://raw.githubusercontent.com/cleverg0d/threat-feeds/main/feeds/url.txt` |

---

### 🔧 How to Configure in FortiGate (GUI)

Repeat the steps below for each feed type:

1. Go to **Security Fabric → External Connectors**  
2. Click **Create New** → Select feed type:  
   - `IP Address`  
   - `Domain Name`  
   - `URL`

3. Set the following:
   - **Name**: e.g. `blocklist-IPs`, `blocklist-domains`, `blocklist-urls`
   - **Update method**: `External feed`
   - **URL**: Paste one of the links above
   - **Status**: `Enable`

4. Save and wait for the connection status to turn green ✅

---

### 🛡️ Use in Policy or Filtering

Once added, feeds can be used in:
- **IPv4 Policies**
- **Web Filtering / DNS Filtering**
- **Threat Feed-based Address/URL objects**
- **DoS / IPS policies**

Monitor entries via:
**Log & Report → External Threat Feed**

---

ℹ️ Tip: The feeds are automatically updated daily via GitHub Actions.
---

## 🧩 Contributions

Pull requests are welcome — feel free to suggest new feeds or improvements.

---
© 2025 [cleverg0d](https://github.com/cleverg0d) • Open Threat Intelligence Initiative
