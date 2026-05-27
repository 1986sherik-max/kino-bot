import telebot

TOKEN = "8778523615:AAHvknRCnbKmbvbb809HTQDW9n1AzKJJtH8"

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(content_types=['all'])
def test(message):

    print(message)

    if message.forward_from_chat:
        print("KANAL ID:")
        print(message.forward_from_chat.id)

bot.infinity_polling()
