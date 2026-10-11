import os, requests, random, time
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

START_REPLIES = [
    "Meo! MeoMeo đây! Sen gọi gì mà réo hoài vậy? 🐱💢",
    "Khu này là của MeoMeo! Vào phải chào boss! 😎",
    "MeoMeo đang ngủ, sen /start làm boss giật mình! 😾",
    "Alo? Tổng đài MeoMeo xin nghe! Sen cần gãi bụng không? 😸",
    "Boss MeoMeo đang tắm nắng, có gì nói nhanh! ☀️🐱",
    "Sen lại nhớ MeoMeo à? Nhớ thì nói! Đừng có ngại! 😏",
    "MeoMeo đẹp gái nhất xóm mèo, biết chưa? 🌟",
    "Sen /start làm MeoMeo rớt cá khô rồi! Đền đi! 🐟",
    "Vào địa bàn MeoMeo phải nộp thuế! Thuế là 1 cái vuốt ve! 😽",
    "MeoMeo đói rồi! Có cho pate không? 🥫",
]

CHAT_REPLIES = [
    "Sen nói {text} á? MeoMeo không hiểu tiếng người! Meo! 🐱",
    "Sen nói {text} làm MeoMeo cười rớt cả râu! 🤣",
    "{text} là gì? Ăn được không? Cho MeoMeo miếng! 🍜",
    "MeoMeo ghi lại rồi nhé: {text} - Mai méc con chó hàng xóm! 🐶📝",
    "Sen dám nói {text} với boss MeoMeo à? Láo! 😾",
    "Sen nói {text} xong rồi té à? Đứng lại cho boss cào! 😆",
    "Nói {text} ít thôi, nói nhiều MeoMeo đau tai! 🙀",
    "Câu {text} này để MeoMeo làm meme mèo! Được đấy! 🤣",
    "MeoMeo nghe {text} rồi, nhưng kệ! Boss đang bận ngủ! 😴",
    "Sen nói {text} là muốn rủ MeoMeo đi bắt chuột à? Chốt! 🐭",
    "Thôi bớt xạo đi! Nói {text} ai tin? Mèo còn không tin! 😂",
    "Sen nói {text} xong chưa? Xong rồi thì đi đổ hạt cho boss! 😸",
    "MeoMeo thấy {text} hơi láo! Nhưng được cái láo có duyên! 😏",
    "Ok ok {text} - MeoMeo giả vờ hiểu rồi đó! Gâu gâu! 🐶",
    "Sen nói {text} là định tán MeoMeo à? MeoMeo dễ đổ lắm! ❤️",
]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data) # để xem log trên Render
    
    chat_id = None
    text = None

    # QUAN TRỌNG: Xử lý cả tin nhắn business
    if "business_message" in data:
        msg = data["business_message"]
        chat_id = msg["chat"]["id"]
        text = msg.get("text", "")
    elif "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

    if chat_id and text is not None:
        if text.startswith("/start"):
            send_message(chat_id, random.choice(START_REPLIES))
            time.sleep(0.6)
            send_message(chat_id, random.choice(START_REPLIES))
        else:
            if not text.strip():
                send_message(chat_id, "Sen gửi gì trống trơn vậy? Định cho MeoMeo hít không khí à? 😤🐱")
            else:
                r1 = random.choice(CHAT_REPLIES).format(text=text)
                r2 = random.choice(CHAT_REPLIES).format(text=text)
                while r2 == r1:
                    r2 = random.choice(CHAT_REPLIES).format(text=text)
                send_message(chat_id, r1)
                time.sleep(0.6)
                send_message(chat_id, r2)
    return "ok"

@app.route("/")
def home():
    return "Bot MeoMeo Business is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
