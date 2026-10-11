import os
import random
import time
from flask import Flask, request
import telebot

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN chưa set trong Render!")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

REPLIES = [
    "alo cái l gì, bố mày đang ngủ 😴",
    "gì? nói nhanh bố còn đi ỉa",
    "ủa alo? nhầm số rồi má",
    "sủa lẹ lên, tao bận lắm",
    "đm ai đây? nói!",
    "gì nữa? tao đang chơi game",
    "bận rồi, tí rep",
    "mày là ai? tao không quen"
]

@app.route('/')
def home():
    return "MeoMeo is Live! Meo meo 😼"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("=== NEW UPDATE ===")
    print(data)
    
    try:
        # 1. Tin nhắn Business (khách nhắn vào nick chính của mày)
        if 'business_message' in data:
            msg = data['business_message']
            chat_id = msg['chat']['id']
            business_connection_id = msg['business_connection_id']
            text = msg.get('text', '')

            # Không tự rep chính mình
            if msg.get('from', {}).get('is_bot'):
                return "ok"

            print(f"Business msg từ {chat_id}: {text}")

            r1 = random.choice(REPLIES)
            r2 = random.choice(REPLIES)
            
            # BẮT BUỘC phải có business_connection_id mới rep được bằng nick Tún nè
            bot.send_message(chat_id, r1, business_connection_id=business_connection_id)
            time.sleep(1.2)
            bot.send_message(chat_id, r2, business_connection_id=business_connection_id)
            return "ok"

        # 2. Tin nhắn thường (nhắn trực tiếp vào bot)
        if 'message' in data:
            msg = data['message']
            chat_id = msg['chat']['id']
            print(f"Normal msg từ {chat_id}")
            bot.send_message(chat_id, random.choice(REPLIES))
            return "ok"

    except Exception as e:
        print(f"LỖI: {e}")
    
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
