import telebot

TOKEN = "8778523615:AAHvknRCnbKmbvbb809HTQDW9n1AzKJJtH8"

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(func=lambda message: True)
def test(message):
    print(message.text)

bot.infinity_polling()
