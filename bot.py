import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def test(message):
    print(message)

bot.infinity_polling()
