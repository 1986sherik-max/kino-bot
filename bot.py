import telebot

TOKEN = "TOKENINGIZ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True, content_types=['any'])
def test(message):

    print(message)

    if message.forward_origin:
        bot.reply_to(message, "FORWARD KELDI ✅")
    else:
        bot.reply_to(message, "Oddiy xabar")

print("Bot ishladi")

bot.infinity_polling()
