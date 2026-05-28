import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(content_types=['all'])
def test(message):

    print("====== MESSAGE ======")

    print(message)

    if message.forward_from_chat:
        print("KANAL ID:")
        print(message.forward_from_chat.id)

bot.infinity_polling(skip_pending=True)
