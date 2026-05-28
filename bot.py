import telebot
from flask import Flask, request

TOKEN = "8778523615:AAG_GafD8K-M6joaswuWM4i985sI1N_YP5s"

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(func=lambda message: True)
def test(message):

    print(message)
    if message.forward_from_chat:
        bot.reply_to(
            message,
            f"Kanal ID: {message.forward_from_chat.id}"
        )
    bot.reply_to(message, "Бот заработает через 3 часа.")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def index():
    return 'Bot ishlayapti'

bot.remove_webhook()

bot.set_webhook(
    url=f"https://kino-bot-production-1071.up.railway.app/{TOKEN}"
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
