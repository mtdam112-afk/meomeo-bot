import os, requests, random
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

START_REPLIES = [
    "Khu này của tao! Vào không chào tao cho chó nó cắn giờ! 🐕",
    "Mày biết bố mày là ai không? Là thằng vừa ỉa xong chưa rửa tay! 💩",
    "Đại ca Minh Tuấn đang bận gãi mông, có gì nói với đệ! 🤣",
    "Mày /start phát tao tưởng công an ập vào, giật cả mình! 👮‍♂️",
    "Vào địa bàn tao phải nộp thuế! Thuế là 1 cái nịnh thối! 😏",
    "Tao là trùm KYC, trùm luôn cả xóm trọ! Ai hỏi gì hỏi đi! 🏠",
    "Mày nhìn đểu tao à? Nhìn nữa tao nhìn lại giờ! 👀",
    "Giang hồ mõm đây! Đụng là chạm, chạm là... trượt chân té! 🤕",
    "Tao vừa ngủ dậy, mồm còn thối, nói nhanh còn kịp! 😴",
    "Alo? Mày là ai? Mẹ mày có biết mày /start lung tung không? 😂",
    "Đại ca đang bận soi gương vì quá đẹp trai! Đợi tí! 🪞",
    "Mày có biết tao là ai không? Tao không biết luôn! 😆",
    "Vào đây phải ngoan, không tao bắt đi rửa bát! 🍽️",
    "Tao đang ăn mì tôm, nói nhanh không tao húp hết! 🍜",
    "Mày /start làm tao rớt cái điện thoại xuống bồn cầu rồi! 📱🚽",
    "Trùm Thái Nguyên đây! Muốn làm ăn phải qua tao, qua bà hàng xóm nữa! 👵",
    "Mày là gà à? Gà thì vào nồi! Thóc thì tao nhặt cho gà ăn! 🐔",
    "Đừng để tao nóng! Tao nóng là tao... cởi áo! Nóng vcl! 🥵",
    "Nghe danh Minh Tuấn chưa? Chưa nghe thì search Google đi, tao cũng chưa có! 😅",
    "Mày gọi tao à? Tao đang bận chém gió với mấy con chó! 🐶",
    "Vào việc nhanh, tao còn phải đi thả diều! 🪁",
    "Tao là dân chơi hệ... hết tiền! Có gì cho vay không? 💸",
    "Mày /start 1 phát nữa là tao yêu mày luôn đó! Cảnh báo rồi! ❤️",
    "Bố mày nhịn lâu lắm rồi đấy! Nhịn ỉa 2 tiếng rồi! 💩",
    "Mày muốn gì? Muốn va hay muốn... vào làm đệ tao? 🤝",
    "Tao đang ngồi trên ngai vàng... bồn cầu! Nói đi! 👑🚽",
    "Gọi gì? Tao đang bận xem TikTok mấy em nhảy! 🕺",
    "Ê cu! Vào chào đại ca 1 tiếng cho phải phép! 😎",
    "Đại ca đây! Có chuyện gì? Mất chó hay mất mèo? 🐱",
    "Mày /start như đúng rồi! Làm như thân lắm! 😏",
    "Tao là giang hồ nhưng giang hồ tình cảm! Ai chửi tao tao khóc! 😭",
    "Khu này tao bảo kê! Ai đụng mày thì... kệ mày! Liên quan gì tao! 😂",
    "Mày non lắm! Theo anh đi, anh chỉ cho cách... bùng nợ! 😆",
    "Tao vừa oánh rắm xong, thơm lắm! Mày có ngửi thấy không? 💨",
    "Vào đây không chào là tao cho ăn đấm... bốc! Đấm bốc là môn thể thao! 🥊",
    "Mày biết luật không? Luật là tao là luật! 😤",
    "Đang yên đang lành /start làm gì? Rảnh à? Rảnh thì đi rửa bát cho mẹ! 🧹",
    "Tao là trùm cuối! Trùm cuối xóm! Xóm tao có 3 nhà! 🏘️",
    "Mày /start phát nữa tao tụt quần chạy quanh xóm giờ! 👖",
    "Nói nhanh! Tao còn phải đi xin tiền mẹ! 🙏",
    "Đại ca Minh Tuấn đẹp trai khoai to đây! Cần gì? 😎",
    "Mày là ai? Người yêu cũ à? Tao block hết rồi mà! 🚫",
    "Giang hồ mõm nhưng được cái... mõm to! Nói đi! 📢",
    "Tao đang bận đếm sao trên trời, mày /start làm tao quên hết rồi! ⭐",
    "Vào đây là phải cười! Không cười tao chọc lét! 🤣"
]

OTHER_REPLIES = [
    "Mày nói {text} á? Nói như cứt! Nhưng mà tao thích! 💩❤️",
    "Thằng này nói {text} nghe ngứa đít thế nhỉ? 😆",
    "Mày nói {text} là định khịa tao à? Tao khịa lại giờ! 😤",
    "Ghi lại rồi nhé! {text} - mai tao mang ra chợ kể! 📢",
    "Mày nói {text} làm tao cười ỉa! Cười thật đấy! 🤣💩",
    "Ủa {text} là cái gì? Ăn được không? Cho tao miếng! 🍔",
    "Mày nói {text} xong rồi té à? Đứng lại coi! 🏃",
    "Thôi mày im mẹ mồm đi! Nói {text} ai hiểu? 😂",
    "Mày nói {text} nghe như triết lý! Triết lý cùi bắp! 😏",
    "Ok ok {text} - tao giả vờ hiểu rồi đó, hài lòng chưa? 🤓",
    "Mày nói {text} làm tao cảm động muốn ỉa luôn! 🥹💩",
    "Nói nữa đi! Nói {text} nữa tao block thật đó! 😆",
    "Mày nói {text} là muốn rủ tao đi nhậu à? Chốt luôn! 🍻",
    "Tao nghe {text} rồi, nhưng tao kệ! Hehe! 😜",
    "Mày nói {text} nghe ngu ngu nhưng mà cute! 😍",
    "Thôi đừng xạo lồn nữa! Nói {text} ai tin? 😂",
    "Mày nói {text} xong chưa? Xong rồi thì đi ngủ đi! 😴",
    "Câu {text} này tao sẽ khắc lên bia mộ mày! Nhớ đấy! 🪦😆",
    "Mày nói {text} làm tao nhớ nyc! Nhớ xong muốn ỉa! 🤣",
    "Giang hồ không nói nhiều! Mày nói {text} là tao ghim! 📌"
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
                send_message(chat_id, "Gửi cái gì trống trơn vậy? Gửi cứt à? 💩")
            else:
                send_message(chat_id, random.choice(OTHER_REPLIES).format(text=text))
    return "ok"

@app.route("/")
def home():
    return "Bot bua cua Minh Tuan is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
