from bs4 import BeautifulSoup
import requests
import telebot

bot = telebot.TeleBot("866798529:AAF_PnyLlZUhHR3SO08z-FFUAHtUKm1Xs38")
chat_id = '-1001206108788'

@bot.message_handler(func=lambda m: True)
def image(message):
    print("Query : ",message.text)
    query = message.text
    query_url =" https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    re = requests.get(query_url)
    soup = BeautifulSoup(re.text,'lxml')
    this = soup.find('img')['src']
    bot.send_message(chat_id,query)
    bot.send_photo(chat_id,this)
bot.polling()
