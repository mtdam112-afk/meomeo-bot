import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
TOKEN = os.environ.get("BOT_TOKEN")
REPLY = "MeoMeo đây 🐱 Chủ đang bận xíu, bạn để lại lời nhắn nhé!"
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.business_message:
        await context.bot.send_message(chat_id=update.business_message.chat_id, text=REPLY, business_connection_id=update.business_message.business_connection_id)
    elif update.message:
        await update.message.reply_text(REPLY)
app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle))
print("MeoMeo da online!")
app.run_polling()
