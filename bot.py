import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

bot.remove_webhook()

@bot.message_handler(content_types=['text'])
def test(message):

    if message.forward_from_chat:
        bot.reply_to(message, f"Kanal posti keldi ✅\n\nKanal: {message.forward_from_chat.title}")
    else:
        bot.reply_to(message, "Oddiy xabar keldi")

print("Bot ishga tushdi...")

bot.infinity_polling(skip_pending=True)
