import os
import requests
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "Gì? Tao đang tắm! Có gì sủa lẹ lên! 🐱💢")
        elif "ai" in text.lower():
            send_message(chat_id, "Tao là trùm cuối, hỏi lắm vcl!")
        elif "ngu" in text.lower():
            send_message(chat_id, "Mày mới ngu ấy, tao khôn vcl ra!")
        else:
            send_message(chat_id, f"Nói gì đấy? Nói lại bố mày nghe xem: {text} 😏")
    return "ok"

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
