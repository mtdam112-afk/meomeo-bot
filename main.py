import os, requests, random
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

# List câu trả lời láo mà hay
START_REPLIES = [
    "Gì? Tao đang tắm! Có gì sủa lẹ lên! 🐱💢",
    "Ủa gọi gì? Tao đang bận đếm tiền lẻ! 😏",
    "Sủa đi, bố mày nghe đây! 🐶",
    "Mày lại nhớ tao à? Nói nhanh tao còn đi ngủ! 😴",
    "Alo alo, tổng đài MeoMeo xin nghe! 📞",
    "Bận rồi, có gì để lại stk tao chuyển khoản sự im lặng cho! 💸",
    "Gọi hoài, tao block giờ! Đùa thôi, nói đi cưng 😆",
    "Vào việc luôn đi bạn êi, lòng vòng vcl! 🤣"
]

OTHER_REPLIES = [
    "Nói gì đấy? Nói lại bố mày nghe xem: {text} 😏",
    "Mày nói tiếng người đi, tao không hiểu tiếng ngoài hành tinh! 👽",
    "Ghi lại rồi, mai tao méc sếp! 😂",
    "Ủa nói gì? Mạng lag quá tao không nghe! 📶",
    "Ok ok, tao giả vờ hiểu rồi đó! 🤓",
    "Thôi mày im đi, nói câu nào dốt câu đó! 😜"
]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text.startswith("/start"):
            reply = random.choice(START_REPLIES)
            send_message(chat_id, reply)
        else:
            reply_template = random.choice(OTHER_REPLIES)
            send_message(chat_id, reply_template.format(text=text))
    return "ok"

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
