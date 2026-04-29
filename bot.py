import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

films = {
    "1001": "BAACAgIAAxkBAAMiae00S8YJ85OWAAE0bP4Tz-YKfp9tAAIpngAC7eNoSzqJJJsi-m4iOwQ",
    "1002": "BAACAgIAAxkBAAM5ae0292fWNdi2exkHGTz4jMXv6CMAAlSfAALt42hLr8tJYe1cFsc7BA",
    "1003": "BAACAgIAAxkBAAM7ae03T7Xc_4tLXDuAsDTLrffQZFgAAqmiAALt42hLh2oFoxNO8-o7BA"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Kino kodini yuboring")

@bot.message_handler(func=lambda message: True)
def send_film(message):
    code = message.text.strip()

    if code in films:
        bot.send_video(message.chat.id, films[code])
    else:
        bot.send_message(message.chat.id, "❌ Bunday kino topilmadi")
@bot.message_handler(content_types=['video'])
def get_id(message):
    bot.send_message(message.chat.id, message.video.file_id)
    bot.infinity_polling()
