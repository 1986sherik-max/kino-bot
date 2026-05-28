import telebot
import os
import time

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

while True:
    try:
        bot.remove_webhook()

        @bot.message_handler(content_types=['all'])
        def test(message):

            print("====== MESSAGE ======")

            try:
                print(message.forward_from_chat.id)
            except:
                print("FORWARD YOQ")

        bot.infinity_polling(timeout=30, long_polling_timeout=10)

    except Exception as e:
        print(e)
        time.sleep(5)
