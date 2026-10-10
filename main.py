import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import asyncio

TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

# Tạo application Telegram
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("Meo meo bot sống rồi nè!")

async def echo(update: Update, context):
    await update.message.reply_text(f"Bạn nói: {update.message.text}")

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@app.route("/webhook", methods=["POST"])
def webhook():
    # Nhận tin nhắn từ Telegram
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok"

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
