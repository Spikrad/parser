import random

import requests
import telebot
from bs4 import BeautifulSoup as b

from time import sleep

URL = 'https://www.anekdot.ru/release/anekdot/day/'

api = ''

def parser(url):
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    anek = soup.find_all('div', class_='text')

    return [a.text for a in anek]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def hello(message):
    a = parser(URL)
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def jokes(message):

    while True:
        if message.text.lower() in 'привет':
            bot.send_message(message.chat.id, list_of_jokes[0])
            del list_of_jokes[0]
        else:
            bot.send_message(message.chat.id, 'Введи привет')

        sleep(15)



bot.polling()
