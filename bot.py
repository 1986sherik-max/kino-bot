import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Ishlayapman ✅")

print("Bot started")

bot.infinity_polling()
