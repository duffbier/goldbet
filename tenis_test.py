import requests

BASE = "https://www.goldbet.it/api/v1/sports"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_tennis_competitions():
    url = f"{BASE}/2/competitions"  # sportId = 2 (tenis)
    resp = requests.get(url, headers=HEADERS)
    print("Status code:", resp.status_code)
    data = resp.json()
    for c in data.get("competitions", [])[:10]:
        print(c["description"])

get_tennis_competitions()
