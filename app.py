
from flask import Flask, request
import requests
import os
 
app = Flask(__name__)
 
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
 
def send_discord(msg):
    if not DISCORD_WEBHOOK:
        return
 
    try:
        requests.post(
            DISCORD_WEBHOOK,
            json={"content": msg},
            timeout=5
        )
    except:
        pass
 
@app.route("/", methods=["GET"])
def home():
    return "NQ Bot Running", 200
 
@app.route("/webhook", methods=["POST"])
def webhook():
 
    data = request.get_json(force=True)
 
    send_discord(
        f"NQ SIGNAL\n\n{data}"
    )
 
    return "ok", 200
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
