import os, requests, random
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

START_REPLIES = [
    "Khu này là của tao! Vào phải /start chào đại ca đàng hoàng chứ! 😎",
    "Mày biết bố mày là ai không? Là đệ của Minh Tuấn! 🫡",
    "Alo? Đại ca Minh Tuấn đang bận đếm tiền, có gì nói với đàn em tao đây! 💸",
    "Vào địa bàn tao mà không chào à? Láo nháo tao cho ra đảo giờ! 🏝️",
    "Mày là thằng nào? Khai mau! Tên tuổi, địa chỉ, số Tele! 😤",
    "Chào đại ca! Em mới vào nghề, có gì đại ca chỉ bảo! 🙏",
    "Đứng lại! Muốn qua phải nộp phí! Phí là 1 câu nịnh! 😆",
    "Tao là trùm khu này! Muốn làm ăn thì phải qua tao! - Minh Tuấn said! 👑",
    "Mày nhìn gì? Nhìn đểu à? /start lại cho tử tế coi! 👀",
    "Giang hồ mõm đây! Đụng là chạm, chạm là... chạy! 🏃‍♂️",
    "Đại ca tao là @mih_tun, còn tao là đệ cứng! Có gì nói! 🔪 (dao nhựa)",
    "Mày có biết luật giang hồ không? Luật là phải lễ phép với tao! 😌",
    "Khu Thái Nguyên này tao bảo kê! Muốn yên ổn thì chào tao 1 tiếng! 😏",
    "Mày mới vào nghề à? Non lắm em ơi! Đi theo anh! 😎",
    "Tao đang ngồi uống trà đá với các anh lớn, có gì nói nhanh! 🍵",
    "Nghe danh Minh Tuấn chưa? Chưa thì giờ biết rồi đó! 🔥",
    "Mày thích gây sự à? Tao gọi 500 anh em đến giờ! (trong game) 🎮",
    "Bố mày nhịn lâu lắm rồi đấy nhé! Nói nhanh trước khi bố mày đổi ý! 💢",
    "Vào đây phải ngoan! Đại ca thương! Hư là đại ca... block! 🚫",
    "Mày là gà hay là thóc? Gà thì tao thịt, thóc thì tao nhặt! 🐔",
    "Đừng để tao nóng! Tao nóng lên là tao... bật điều hòa! ❄️",
    "Trông mặt mày uy tín đấy! Theo đại ca Minh Tuấn làm KYC đi! 💼",
    "Nói ít, làm nhiều! Giang hồ là phải thế! Vào việc! 🤝",
    "Mày có số má gì không? Không thì đi theo tao cho có số! 🔢",
    "Tao là dân chơi hệ hiền! Động vào tao là tao... méc đại ca! 😂"
]

OTHER_REPLIES = [
    "Mày nói {text} là có ý gì? Cà khịa tao à? 😤",
    "Câu {text} này nghe ngứa tai nhỉ? Muốn va không? 😏",
    "Mày nói linh tinh gì đấy? Nói lại tao nghe cho rõ! 👂",
    "Thằng này láo! Dám nói {text} với đại ca à? 😠",
    "Được, câu {text} này tao ghim! Mai tính! 📌",
    "Mày đang thử lòng tao đấy à? {text} á? Non! 😌",
    "Nói câu {text} xong rồi chuồn à? Đứng lại! 😆",
    "Mày nói {text} là ý gì? Muốn vào băng tao à? Ok duyệt! ✅",
    "Giang hồ không nói nhiều! Nói {text} là phải làm! Làm đi! 💪",
    "Câu này được đấy! Đại ca Minh Tuấn sẽ thích thằng như mày! 😎",
    "Mày nói {text} nghe cũng máu đấy! Theo tao! 🔥",
    "Thôi bớt xạo đi! Nói {text} ai tin? 😂"
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
            t = random.choice(OTHER_REPLIES)
            send_message(chat_id, t.format(text=text))
    return "ok"

@app.route("/")
def home():
    return "Bot giang ho cua Minh Tuan is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
