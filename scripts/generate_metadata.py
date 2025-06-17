import os
import json
from datetime import datetime

feeds_dir = os.path.join(os.path.dirname(__file__), '..', 'feeds')
metadata_path = os.path.join(feeds_dir, 'metadata.json')

metadata = {
    "updated_at": datetime.utcnow().isoformat() + "Z",
    "counts": {}
}

for file in os.listdir(feeds_dir):
    if file.endswith(".txt"):
        full_path = os.path.join(feeds_dir, file)
        with open(full_path, "r") as f:
            lines = sum(1 for _ in f)
            metadata["counts"][file] = lines

with open(metadata_path, "w") as f:
    json.dump(metadata, f, indent=2)

print(f"[+] metadata.json written to {metadata_path}")