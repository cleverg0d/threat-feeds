
import requests
import os
import re
import json

# Папка с результатами
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'feeds')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Загрузка источников из sources.json
with open(os.path.join(os.path.dirname(__file__), '..', 'sources.json')) as f:
    SOURCES = json.load(f)

def fetch(url):
    try:
        print(f"[.] Fetching: {url}")
        resp = requests.get(url, timeout=20)
        if resp.ok:
            print(f"[+] Fetched {len(resp.text.splitlines())} lines from {url}")
            return resp.text
        else:
            print(f"[!] Failed with HTTP {resp.status_code}: {url}")
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

    for url in SOURCES.get("ip", []):
        data = fetch(url)
        all_ips.update(extract_ips(data))

    for url in SOURCES.get("url", []):
        data = fetch(url)
        all_urls.update(extract_urls(data))

    for url in SOURCES.get("domain", []):
        data = fetch(url)
        all_domains.update(extract_domains(data))

    print(f"\n=== Summary ===")
    print(f"[+] IPs collected: {len(all_ips)}")
    print(f"[+] Domains collected: {len(all_domains)}")
    print(f"[+] URLs collected: {len(all_urls)}")

    save_to_file("ip.txt", all_ips)
    save_to_file("url.txt", all_urls)
    save_to_file("domain.txt", all_domains)

if __name__ == "__main__":
    main()
