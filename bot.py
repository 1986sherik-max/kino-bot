import telebot
from flask import Flask, request

TOKEN = "8778523615:AAG_GafD8K-M6joaswuWM4i985sI1N_YP5s"

CHANNEL_ID = -1003790400720

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Kino kodlari
movies = {
    "101": 3,
    "102": 6,
    "103": 7
}


@bot.message_handler(func=lambda m: True)
def send_movie(message):

    code = message.text.strip()

    if code in movies:

      bot.copy_message(
    chat_id=message.chat.id,
    from_chat_id=CHANNEL_ID,
    message_id=movies[code]
)

    else:
        bot.reply_to(message, "Kino topilmadi ❌")


@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():

    json_str = request.get_data().decode('UTF-8')

    update = telebot.types.Update.de_json(json_str)

    bot.process_new_updates([update])

    return 'ok', 200


@app.route('/')
def index():
    return 'Bot ishlayapti ✅'


bot.remove_webhook()

bot.set_webhook(
    url=f"https://kino-bot-production-1071.up.railway.app/{TOKEN}"
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
