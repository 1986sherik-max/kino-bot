import telebot

TOKEN = "8778523615:AAHvknRCnbKmbvbb809HTQDW9n1AzKJJtH8"

bot = telebot.TeleBot(TOKEN)

movies = {
    "1002": 3,
    "1002": 26,
}

CHANNEL_ID = -1001234567890


@bot.message_handler(func=lambda message: True)
def send_movie(message):

    code = message.text.strip()

    if code in movies:

        bot.forward_message(
            chat_id=message.chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=movies[code]
        )

    else:
        bot.send_message(message.chat.id, "Kino topilmadi")


@bot.message_handler(content_types=['forward_from_chat'])
def test(message):
    print(message.forward_from_chat.id)


bot.infinity_polling()
