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
    response = requests.get(url, proxies=proxies, timeout=10)

    return f"Status: {response.status_code}\n{response.text[:500]}"
