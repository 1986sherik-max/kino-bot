import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(content_types=['text'])
def test(message):
    bot.reply_to(message, "Salom! Bot ishlayapti ✅")

print("Bot ishga tushdi...")

bot.infinity_polling(skip_pending=True)
