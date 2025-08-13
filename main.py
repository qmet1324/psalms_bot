import os
import requests

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

bot.set_my_commands(
    commands = [
        telebot.types.BotCommand('hello', 'Say Hi to PsalmsBot'),
        telebot.types.BotCommand('verse', 'Receive a random psalm'),
    ],
)

@bot.message_handler(commands=['hello'])
def send_verse(message):
    bot.reply_to(message, "Greetings, the Son of God") 

@bot.message_handler(commands=['verse'])
def send_verse(message):
    response = requests.get("https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-asv/books/genesis/chapters/1/verses/1.json")
    data = response.json()
    bot.reply_to(message, data["text"])

bot.infinity_polling()
