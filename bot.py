import telebot
from flask import Flask, request

TOKEN = "8778523615:AAFG5oRO6LrLOvBKeOIUhweOwCnZvLUNbBo"

CHANNEL_ID = -1003790400720

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Kino kodlari
movies = {
    "1001": 3,
    "1015": 4,
    "1002": 5,
     "1003": 6,
    "1004": 7,
    "1006": 8,
    "1007": 9,
    "1008": 10,
    "1005": 11,
     "1009": 12,
    "1010": 13,
    "1011": 14,
    "1012": 15,
    "1013": 16,
    "1014": 17,
     "1016": 18,
     "1017": 19,
     "1018": 20,
     "1019": 21,
     "1020": 22,
     "1021": 23,
     "1022": 24,
     "1023": 25,
     "1024": 26,
     "1025": 27,
     "1026": 28,
     "1027": 29,
     "1028": 30,
     "1029": 31,
    "1030": 32,
    "1031": 33,
    "1032": 34,
     "1033": 35,
    "1034": 36,
    "1035": 37,
    "1036": 38,
    "1037": 39,
    "1038": 40,
     "1039": 41,
    "1040": 42,
    "1041": 43,
    "1042": 44,
    "1043": 45,
    "1044": 46,
     "1045": 47,
     "1046": 48,
     "1047": 49,
     "1048": 50,
     "1049": 51,
     "1050": 52,
     "1051": 53,
     "1052": 54,
     "1053": 55,
     "1054": 56,
     "1055": 57,
     "1056": 58,
     "1057": 59,
     "1058": 60
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
        bot.reply_to(message, "Noto'g'ri kod kiritdingiz ❌ / Вы ввели неверный код ❌")


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
