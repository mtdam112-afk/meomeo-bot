import os, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
class H(BaseHTTPRequestHandler):
 def do_GET(self):
  self.send_response(200);self.end_headers();self.wfile.write(b"MeoMeo bot is running!")
 def log_message(self,*a): return
threading.Thread(target=lambda: HTTPServer(("0.0.0.0", int(os.environ.get("PORT",10000))), H).serve_forever(), daemon=True).start()
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
TOKEN = os.environ.get("BOT_TOKEN")
REPLY = "MeoMeo đây 😺 Chủ đang bận xíu, nhắn lại sau nha!"
async def handle(update: Update, context):
    if update.business_message:
        await context.bot.send_message(chat_id=update.business_message.chat_id, text=REPLY)
    elif update.message:
        await update.message.reply_text(REPLY)
app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle))
print("MeoMeo da online!")
app.run_polling()
