
from email import header
from urllib import request
import telebot
bot = telebot.TeleBot('5354946840:AAG-puracD5c7qbG2A7mOs3d6xJhu_Nafg4')

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Lala')



bot.polling(none_stop=True)



# --- 

import requests

token = '5354946840:AAG-puracD5c7qbG2A7mOs3d6xJhu_Nafg4'
chat_id = '46471720'

def send(text):
    global token, chat_id
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    return requests.get(url)



url = f'https://api.telegram.org/bot{token}/getUpdates'
res = requests.get(url)
print(res.text)



# --- datatime ---

import datetime, time
messageTime = 1659339201
messageTime = datetime.datetime.utcfromtimestamp(messageTime)
messageTime = messageTime.strftime('%Y-%m-%d %H:%M:%S')
