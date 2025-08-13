import os
import requests

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['verse'])
def send_verse(message):
    response = requests.get("https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-asv/books/genesis/chapters/1/verses/1.json")
    data = response.json()
    bot.reply_to(message, data["text"])

# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

bot.infinity_polling()
