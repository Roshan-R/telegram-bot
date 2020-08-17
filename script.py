import telebot,urllib.request,urllib.parse,re,requests 
from telebot import apihelper 
import os

chat_id = os.environ.get('chat_id')
TG_PROXY = os.environ.get('TG_PROXY')
TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')

apihelper.proxy = {'http': TG_PROXY}

bot = telebot.TeleBot(TG_BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def image(message):
    print("Query : ",message.text)
    urlopenheader={ 'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    request_url='https://www.bing.com/images/async?q=' + message.text.replace(' ','%20') + '&count=35&adlt=off'
    request=urllib.request.Request(request_url,None,headers=urlopenheader)
    response=urllib.request.urlopen(request)
    html = response.read().decode('utf8')
    links = re.findall('murl&quot;:&quot;(.*?)&quot;',html)
    print(links[0])
    bot.send_photo(chat_id,links[0])
bot.polling(none_stop=True,timeout=123)
