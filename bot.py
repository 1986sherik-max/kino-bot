import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(func=lambda m: True, content_types=[
    'text',
    'audio',
    'document',
    'photo',
    'sticker',
    'video',
    'voice',
    'video_note',
    'contact',
    'location',
    'animation'
])
def test(message):

    print("====== MESSAGE KELDI ======")

    print(message)

    try:
        print("KANAL ID:")
        print(message.forward_from_chat.id)
    except Exception as e:
        print("ERROR:")
        print(e)

bot.infinity_polling()
