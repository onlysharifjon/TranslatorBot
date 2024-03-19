import telebot
from googletrans import Translator


TOKEN = ''


bot = telebot.TeleBot(TOKEN)


translator = Translator()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-переводчик. Отправь мне текст, и я переведу его на английский язык.")


@bot.message_handler(func=lambda message: True)
def translate_message(message):

    src_lang = translator.detect(message.text).lang


    translated_text = translator.translate(message.text, src=src_lang, dest='en')


    bot.send_message(message.chat.id, f"Перевод на английский: {translated_text.text}")

bot.polling()