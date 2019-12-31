import telebot
from google_images_download import google_images_download

#defining the bot...
bot = telebot.TeleBot("866798529:AAF_PnyLlZUhHR3SO08z-FFUAHtUKm1Xs38")
chat_id = '-1001206108788'

@bot.message_handler(regexp = 'i:')
def image(message):
    text = message.text.split(':')[1]
    print(text)
    response = google_images_download.googleimagesdownload()
    arg = {"keywords":text,"limit":1}
    path = response.download(arg)
    path = path[0].get(text)[0]
    photo = open(path,'rb')
    bot.send_photo(chat_id,photo)
bot.polling()
