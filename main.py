
import telebot
from googletrans import Translator

#import dotenv
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("API_TOKEN")


bot = telebot.TeleBot(BOT_TOKEN)

translator = Translator()


@bot.message_handler(commands=['start'])
def start_message(message):
    
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}!, Этот бот переводить с русского на Англйский постепена я буду улучшать бота")
    
    bot.send_message(message.from_user.id, "Выберите язык для перевода: Английский")

@bot.message_handler(commands=['creator'])
def creator_message(message):  
    bot.send_message(message.from_user.id, "Создатель бота -- https://t.me/Relae27")  


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    
    text = message.text
    
    is_russian_word = text.isalpha() and all('\u0400' <= char <= '\u04FF' for char in text)
    if is_russian_word:
        
        translated_text = translator.translate(text, dest='en').text
        
        bot.reply_to(message, f"Переведенный текст: {translated_text}")
    else:
        
        bot.reply_to(message, "Пожалуйста, введите только русское слово.")


bot.polling()
