import telebot,urllib.request,urllib.parse,re,requests 
from telebot import apihelper 
from duck_api import search
import os

chat_id = os.environ.get('chat_id')
TG_PROXY = os.environ.get('TG_PROXY')
TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')

apihelper.proxy = {'http': TG_PROXY}

bot = telebot.TeleBot(TG_BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def image(message, index=0):
    """ receives message from bot and sends back first image result from duckduckgo """

    message = message.text

    try:
        result_no = message.split(' ')[-1]
        index = int(result_no)
        message = message[:(-1*len(result_no))]
        print(str(index))

    except Exception as e:
        index = 0
        print(str(e))

    try:
        print("Query : ",message)

        bot.send_photo(chat_id, search(message, index=index))

    except Exception as err:
        print(str(err))
        

bot.polling(none_stop=True,timeout=123)
