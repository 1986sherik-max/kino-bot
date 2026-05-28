import telebot

TOKEN = "8778523615:AAG_GafD8K-M6joaswuWM4i985sI1N_YP5s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def test(message):

    if message.forward_date:
        bot.reply_to(message, "FORWARD KELDI ✅")
    else:
        bot.reply_to(message, "Oddiy xabar")

print("Bot ishladi")

bot.infinity_polling(none_stop=True)
