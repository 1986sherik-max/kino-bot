import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

films = {
    "1001": "VIDEO_ID",
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
    print(message.video.file_id)
bot.infinity_polling()
