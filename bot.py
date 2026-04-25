import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

films = {
    "1001": "BAACAgIAAxkBAAMHaezyG-4i53vQU5XIUtFVDzWErzcAAimeAALt42hLO2p8GZTsnkU7BA",
    "1002": "BAACAgIAAxkBAAMSaez2j76yTGGGLwyhSZEDbPXGJmsAAlSfAALt42hLG7niw1XbCaE7BA",
     "1003": "BAACAgIAAxkBAAM0ae0FjsrU8ldfOWBOKdjx9ykGFuwAAqmiAALt42hLS_mAl8aIjKw7BA"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🎬 Kino kodini yuboring")

@bot.message_handler(func=lambda message: True)
def send_film(message):
    code = message.text.strip()

    if code in films:
        bot.send_video(message.chat.id, films[code])
    else:
        bot.send_message(message.chat.id, "❌ Bunday kino topilmadi")

bot.polling()
