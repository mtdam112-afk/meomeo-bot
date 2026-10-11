import os, random, time, requests
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
app = Flask(__name__)

REPLIES = [
    "alo cái l gì, bố mày đang ngủ 😴",
    "gì? nói nhanh bố còn đi ỉa",
    "ủa alo? nhầm số rồi má",
    "sủa lẹ lên, tao bận lắm",
    "đm ai đây? nói!",
]

def send_business(chat_id, text, business_id):
    # Dùng requests trực tiếp để không bị lỗi thư viện
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "business_connection_id": business_id
    }
    requests.post(url, json=data)

def send_normal(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.route('/')
def home():
    return "MeoMeo Live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    try:
        if 'business_message' in data:
            msg = data['business_message']
            if msg.get('from', {}).get('is_bot'): return "ok"
            chat_id = msg['chat']['id']
            b_id = msg['business_connection_id']
            send_business(chat_id, random.choice(REPLIES), b_id)
            time.sleep(1)
            send_business(chat_id, random.choice(REPLIES), b_id)
            return "ok"
        if 'message' in data:
            msg = data['message']
            chat_id = msg['chat']['id']
            send_normal(chat_id, random.choice(REPLIES))
    except Exception as e:
        print(f"LOI: {e}")
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
