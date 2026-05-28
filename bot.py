import telebot

TOKEN = "8778523615:AAG_GafD8K-M6joaswuWM4i985sI1N_YP5s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def test(message):

    text = str(message.text)

    bot.reply_to(message, f"Siz yozdingiz: {text}")

print("Bot ishladi")

bot.infinity_polling(none_stop=True)
