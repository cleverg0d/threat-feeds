import requests
import os
import re

# Папка с результатами
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'feeds')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Источники фидов
SOURCES = {
    "ip": [
        "https://feodotracker.abuse.ch/downloads/ipblocklist.txt",
        "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset",
        "https://rules.emergingthreats.net/blockrules/compromised-ips.txt",
        "http://malc0de.com/bl/IP_Blacklist.txt"
    ],
    "url": [
        "https://urlhaus.abuse.ch/downloads/text/",
    ],
    "domain": [
        "https://raw.githubusercontent.com/stamparm/blackbook/master/blackbook.txt"
    ]
}

def fetch(url):
    try:
        resp = requests.get(url, timeout=20)
        if resp.ok:
            return resp.text
    except Exception as e:
        print(f"[!] Failed to fetch {url}: {e}")
    return ""

def extract_domains(text):
    raw = re.findall(r'(?:^|\s)([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\s|$)', text)
    return set(d.strip(".,;()[]{}") for d in raw if not d.startswith("http"))

def extract_ips(text):
    return set(re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text))

def extract_urls(text):
    return set(re.findall(r'https?://[^\s]+', text))

def save_to_file(filename, items):
    with open(os.path.join(OUTPUT_DIR, filename), 'w') as f:
        for item in sorted(set(items)):
            f.write(item + '\n')

def main():
    all_ips, all_urls, all_domains = set(), set(), set()

    for url in SOURCES["ip"]:
        data = fetch(url)
        all_ips.update(extract_ips(data))

    for url in SOURCES["url"]:
        data = fetch(url)
        all_urls.update(extract_urls(data))

    for url in SOURCES["domain"]:
        data = fetch(url)
        all_domains.update(extract_domains(data))

    save_to_file("ip.txt", all_ips)
    save_to_file("url.txt", all_urls)
    save_to_file("domain.txt", all_domains)

if __name__ == "__main__":
    main()
