import os
import requests
import random
import telebot
from constants import FIRST_PSALM, LAST_PSALM
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

bot.set_my_commands(
    commands = [
        telebot.types.BotCommand('hello', 'Say Hi to PsalmsBot'),
        telebot.types.BotCommand('psalm', 'Receive a random psalm'),
    ],
)

@bot.message_handler(commands=['hello'])
def send_greetings(message):
    bot.reply_to(message, "Greetings, the Son of God") 

@bot.message_handler(commands=['psalm'])
def send_psalm(message):
    rand_psalm_val = random.randrange(FIRST_PSALM, LAST_PSALM)
    response = requests.get(f"https://bible-api.com/psalms{rand_psalm_val}")
    verses = response.json()
    bot.reply_to(message, verses["text"])

bot.infinity_polling()
