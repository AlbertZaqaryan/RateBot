from telebot import TeleBot
from dotenv import load_dotenv
from RateBot.parse_rate import parsing
import os

load_dotenv()


bot = TeleBot(token=os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_photo(message.chat.id, open('rate_image.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Ողջույն ես RateBot ն եմ, ես կուղարկեմ քեզ օրվա rate երը')


@bot.message_handler(func=lambda message: message.text == "Rates")
def get_rates(message):
    bot.send_message(message.chat.id, 'Loading ...')
    bot.send_message(message.chat.id, parsing())


bot.polling()