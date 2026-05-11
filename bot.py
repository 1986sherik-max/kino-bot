import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

films = {
    "1001": "BAACAgIAAxkBAAMiae00S8YJ85OWAAE0bP4Tz-YKfp9tAAIpngAC7eNoSzqJJJsi-m4iOwQ",
    "1002": "BAACAgIAAxkBAAM5ae0292fWNdi2exkHGTz4jMXv6CMAAlSfAALt42hLr8tJYe1cFsc7BA",
    "1003": "BAACAgIAAxkBAAM7ae03T7Xc_4tLXDuAsDTLrffQZFgAAqmiAALt42hLh2oFoxNO8-o7BA",
    "1004": "BAACAgIAAxkBAAOjafGs8HfsDL1aNjqffjJikarghGcAAqyYAAK-6ZFLP4cDKPsJ3xc7BA",
     "1005": "BAACAgIAAxkBAAPxaf7rqAmusDYaJZpRuiA6R4UhtRgAApOZAAJlkPhLvnA0iWuxwD87BA",
    "1006": "BAACAgIAAxkBAAPZaf7n_hnewVTINqM8Ojzu5JhF1OMAAmWdAAKmybhLndwCgLeJyfI7BA",
    "1007": "BAACAgIAAxkBAAPbaf7oOu_0sK5HwBYHTyIq14rE4lsAAnadAAKmybhL42_vth7lH8Y7BA",
    "1008": "BAACAgIAAxkBAAPdaf7oRnbQtG3PTv8hsf4h-UtAx5QAAqqdAAKmybhL5y6Q2gUUKG07BA",
    "1009": "BAACAgIAAxkBAAP7af9un5iBKdEZ8bk3dmXzXtd5tHQAAp-gAALeD_hL55scGeUgGts7BA",
    "1010": "BAACAgIAAxkBAAP9af9uv2zUS6G-EAdxNDZSbAQLE_UAAqqgAALeD_hL6LLV_u68Dp47BA",
    "1011": "BAACAgIAAxkBAAIBHGn_lKKItPUuRLrqGYOQhkJrGX8GAAJBnQACXXABSCQBycgaieGGOwQ",
    "1012": "BAACAgIAAxkBAAIBHmn_lL21FNoqDnqPNAFLS2g-UCaGAALgngACXXABSE_P9Ln-CtKgOwQ",
    "1013": "BAACAgIAAxkBAAIBvGoAAbX07wAB2nTVwkZ9B5VlXbRKn7IAApyWAAI2zgFILO_vdPGAxYs7BA",
    "1014": "BAACAgIAAxkBAAIB7GoBjOw_mpW7yX35IXs0Cfjm_1TmAALHlQACNs4JSLvMY2hJRrl8OwQ"  
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Kino kodini yuboring")

@bot.message_handler(func=lambda message: True)
def send_film(message):
    code = message.text.strip()

    if code in films:
        bot.send_video(message.chat.id, films[code])
    else:
        bot.send_message(message.chat.id, "❌ Bunday kino topilmadi")
@bot.message_handler(content_types=['video'])
def get_id(message):
    bot.reply_to(message, message.video.file_id)
bot.infinity_polling()
