import requests

def get_tennis_competitions():
    url = "https://www.goldbet.it/api/v1/sportsbook/sports/tennis/competitions"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://www.goldbet.it/",
        "Origin": "https://www.goldbet.it"
    }

    resp = requests.get(url, headers=headers)
    print("Status code:", resp.status_code)

    try:
        data = resp.json()
        print(data)
    except Exception as e:
        print("Response text:", resp.text)
        print("Error:", e)

get_tennis_competitions()

