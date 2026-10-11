import os, requests, random
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

START_REPLIES = [
    "Khu này là của Minh Tuấn! Vào phải chào đại ca! 😎",
    "Mày biết trùm khu này là ai không? Là Minh Tuấn! 👑",
    "Alo? Minh Tuấn đang bận đếm tiền, có gì nói! 💸",
    "Minh Tuấn bảo: Vào đây phải ngoan! 🐶",
    "Đứng lại! Muốn qua phải nịnh Minh Tuấn! 😏",
    "Minh Tuấn đẹp trai nhất hệ mặt trời, biết chưa? 🌟",
    "Mày /start làm Minh Tuấn phải ra mặt, biết sợ chưa? 😤",
    "Vào địa bàn Minh Tuấn phải lễ phép! Không là ăn đấm! 🥊",
    "Minh Tuấn đang ngồi trên đỉnh cao, nhìn xuống thấy mày bé tí! 🏔️",
    "Tao là Minh Tuấn, trùm KYC, chúa tể xóm trọ! 🏠",
    "Minh Tuấn bảo: Muốn làm ăn thì phải qua tao! 💼",
    "Mày nhìn gì? Nhìn đểu Minh Tuấn à? 👀",
    "Minh Tuấn giang hồ nhưng có tiền! Mày có không? 💸",
    "Mày /start làm Minh Tuấn phải rep, biết vinh dự chưa? 😎",
    "Đại ca Minh Tuấn đang bận selfie, có gì nói nhanh! 📸",
    "Vào đây phải tôn trọng Minh Tuấn! Không là block! 🚫",
    "Minh Tuấn nói: Muốn giàu thì theo tao! 💰",
    "Mày là ai? Có phải là fan Minh Tuấn không? 😍",
    "Minh Tuấn đẹp trai quá, làm tao phải /start lại! 😆",
    "Tao Minh Tuấn đây! Có gì nhờ vả không? 🤝",
    "Minh Tuấn bảo kê khu này! Ai dám đụng? 😤",
    "Nghe danh Minh Tuấn chưa? Chưa thì giờ biết! 🔥",
    "Minh Tuấn đang uống trà sữa, có gì nói! 🍵",
    "Mày /start làm Minh Tuấn phải cười! 😂",
    "Minh Tuấn là trùm, mày là thằng... không là gì! 😎",
    "Vào đây phải nói: 'Dạ đại ca Minh Tuấn đẹp trai!' 😆",
    "Minh Tuấn dạy mày cách làm người: Phải biết /start! 🤣",
    "Đại ca Minh Tuấn đang chơi game, đừng làm phiền! 🎮",
    "Minh Tuấn bảo: Muốn sống lâu thì nịnh tao! 😏",
    "Mày biết Minh Tuấn kiếm tiền bằng gì không? Bằng KYC! 💸",
    "Minh Tuấn nói: Ai đẹp trai hơn tao giơ tay! 🙋",
    "Tao Minh Tuấn đây, có gì nhờ vả cứ nói! 🤝",
    "Minh Tuấn đang đếm sao trên trời, đếm đến mày! ⭐",
    "Vào đây phải chào Minh Tuấn 3 tiếng: 'Dạ đại ca!' 🙏",
    "Minh Tuấn là chúa, mày là... nô lệ! 😈",
    "Minh Tuấn bảo: Muốn giàu thì phải học KYC! 💼",
    "Mày /start làm Minh Tuấn phải thở dài... 😌",
    "Đại ca Minh Tuấn đẹp trai quá, làm gì cũng đúng! 😎",
    "Minh Tuấn nói: Ai theo tao sẽ giàu! 💸",
    "Minh Tuấn là ánh sáng, mày là bóng tối! ☀️",
    "Vào đây phải biết: Minh Tuấn là số 1! 🏆",
    "Minh Tuấn bảo: Muốn sống thì phải nghe lời! 😏",
    "Mày biết Minh Tuấn làm gì không? Làm trùm! 👑"
]

OTHER_REPLIES = [
    "Mày nói {text} à? Minh Tuấn không quan tâm! 😎",
    "Mày nói {text} làm Minh Tuấn phải cười! 🤣",
    "Minh Tuấn nghe rồi: {text} - Nghe như cứt! 💩",
    "Mày nói {text} là muốn cà khịa Minh Tuấn à? 😤",
    "Minh Tuấn bảo: Nói {text} ít thôi, nói nhiều đau mồm! 😆",
    "Câu {text} này Minh Tuấn chưa nghe bao giờ! 😏",
    "Mày nói {text} xong rồi thì đi ngủ đi! 😴",
    "Minh Tuấn thấy {text} hơi ngu ngu! 😂",
    "Mày nói {text} làm Minh Tuấn nhớ đời! 🤯",
    "Minh Tuấn bảo: Nói {text} phải có nguồn! 📚",
    "Câu {text} này để Minh Tuấn note lại! 📝",
    "Mày nói {text} làm Minh Tuấn muốn block! 🚫",
    "Minh Tuấn nghe {text} rồi, nhưng kệ mày! 😌",
    "Mày nói {text} làm Minh Tuấn phải rep! 😎",
    "Minh Tuấn bảo: {text} là triết lý cùi! 😆",
    "Mày nói {text} làm Minh Tuấn muốn share! 📢",
    "Minh Tuấn thấy {text} hơi láo! 😤",
    "Mày nói {text} làm Minh Tuấn phải nghĩ... 🤔",
    "Minh Tuấn bảo: Nói {text} phải có lý! 🤓",
    "Câu {text} này Minh Tuấn chưa thấy bao giờ! 😲",
    "Mày nói {text} làm Minh Tuấn cười té ghế! 🤣",
    "Minh Tuấn nghe {text} xong rồi, mày làm gì được tao? 😏",
    "Mày nói {text} làm Minh Tuấn nhớ đời! 😎",
    "Minh Tuấn bảo: Nói ít thôi, làm nhiều đi! 💪",
    "Câu {text} này để Minh Tuấn lưu làm meme! 🤣"
]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text.startswith("/start"):
            send_message(chat_id, random.choice(START_REPLIES))
        else:
            if not text.strip():
                send_message(chat_id, "Mày gửi gì trống trơn vậy? Muốn Minh Tuấn block à? 🚫")
            else:
                send_message(chat_id, random.choice(OTHER_REPLIES).format(text=text))
    return "ok"

@app.route("/")
def home():
    return "Bot cua Minh Tuan is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
