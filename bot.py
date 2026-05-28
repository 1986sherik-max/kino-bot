import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(content_types=['all'])
def test(message):

    print("====== NEW MESSAGE ======")

    try:
        print(message.forward_from_chat.id)
    except:
        print("FORWARD YOQ")

bot.infinity_polling()
