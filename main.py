from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route("/")
def goldbet_tennis():
    proxy_host = os.getenv("PROXY_HOST")
    proxy_port = os.getenv("PROXY_PORT")
    proxy_user = os.getenv("PROXY_USER")
    proxy_pass = os.getenv("PROXY_PASS")

    proxies = {
        "http": f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}",
        "https": f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"
    }

    url = "https://www.goldbet.it/api/v1/sportsbook/sports/tennis/competitions"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.goldbet.it/",
    "Origin": "https://www.goldbet.it",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br"
}

response = requests.get(url, proxies=proxies, headers=headers, timeout=10)


    return f"Status: {response.status_code}\n{response.text[:500]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
