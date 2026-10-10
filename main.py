import os, requests, random
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

START_REPLIES = [
    "Gì? Tao đang tắm! Có gì sủa lẹ lên! 🐱💢",
    "Ủa alo? Đang bận đếm lông mèo! 😏",
    "Sủa đi, bố mày nghe đây!",
    "Lại là mày à? Nhớ tao đến thế à? 😌",
    "Tổng đài MeoMeo xin nghe, mày là đứa thứ 100 gọi hôm nay! 📞",
    "Nói nhanh tao còn đi ngủ, buồn ngủ vcl! 😴",
    "Gọi gì? Có tiền không mà gọi? 💸",
    "Vào việc luôn đi, đừng lòng vòng như Hải Phòng! 🤣",
    "Tao đang ỉa, có gì nói nhanh! 💩",
    "Alo? Mày nói gì tao không nghe, nói to lên!",
    "Gì? Mày định rủ tao đi nhậu à? Chốt! 🍻",
    "Đang bận làm đẹp, có gì mai nói! 💅",
    "Mày là ai? Tao không nhớ! Não cá vàng lắm! 🐟",
    "Ơi? Tao đây! Mày đâu? Lạc à?",
    "Thích tao à mà /start hoài vậy? 😏",
    "Bận lắm, nhưng vì mày đẹp trai/xinh gái nên tao rep đó! 😎",
    "Gọi tao có gì không đại ca? 🫡",
    "Tao đến rồi đây, có quà không? 🎁",
    "Đang load... 99%... Ok nói đi!",
    "Mày gõ /start làm tao giật mình, đang mơ thấy mày đó! 😳",
    "Dạ em nghe! Anh cần gì ạ? (giả vờ ngoan 5s) 😇",
    "Trùm KYC Minh Tuấn đây, cần gì nói! 💼",
    "Tao đang ngồi trên ngai vàng, tâu đi! 👑",
    "Nhanh, wifi chùa sắp hết giờ! 📶",
    "Gọi lắm thế, tính làm phiền tao à? Yêu à? 😜"
]

OTHER_REPLIES = [
    "Nói gì đấy? Nói lại bố mày nghe xem: {text} 😏",
    "Mày nói tiếng người đi, tao chưa học tiếng ngoài hành tinh! 👽",
    "Ghi lại rồi, mai tao méc mẹ mày! 😂",
    "Mạng lag quá, mày nói lại coi! 📶",
    "Ok tao giả vờ hiểu rồi đó, nói tiếp đi! 🤓",
    "Thôi mày im đi, nói câu nào ngáo câu đó! 😜",
    "Câu này hay đấy, để tao đăng Facebook! 📝",
    "Mày vừa nói gì? {text} á? Tao không quan tâm lắm! 😑",
    "Ủa {text} là gì? Ăn được không? 🍜",
    "Tao nghe rồi, nhưng tao kệ! 😌",
    "Nói hay lắm, vỗ tay! 👏👏👏",
    "Văn mẫu à? Copy ở đâu đấy? 😆",
    "Thôi đừng xạo nữa, tao biết hết rồi!",
    "Mày nói nữa là tao yêu mày luôn đó! ❤️",
    "Im lặng là vàng, mày nói là kim cương giả! 💎",
    "Tao đang ghi âm lại để làm bằng chứng! 🎤",
    "Nói ít thôi, nói nhiều đau họng! 🫢",
    "Tao off đây, mày tự chơi 1 mình đi! 🎮"
]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text.startswith("/start"):
            send_message(chat_id, random.choice(START_REPLIES))
        elif text.strip() == "":
            send_message(chat_id, "Gửi gì trống trơn vậy ba? 🤔")
        else:
            template = random.choice(OTHER_REPLIES)
            send_message(chat_id, template.format(text=text))
    return "ok"

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
