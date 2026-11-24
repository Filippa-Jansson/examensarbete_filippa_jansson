import json
from pathlib import Path

import requests

BASE = "https://www.dnd5eapi.co/api/2014"
KLASSER = ["barbarian", "fighter", "ranger", "cleric", "wizard"]
UT = Path("dnd_data/raw")
UT.mkdir(parents=True, exist_ok=True)

for klass in KLASSER:
    svar = requests.get(f"{BASE}/classes/{klass}/levels", timeout=30)
    svar.raise_for_status()
    (UT / f"levels_{klass}.json").write_text(json.dumps(svar.json(), indent=2))
    print(f"{klass}: {len(svar.json())} levels sparade")