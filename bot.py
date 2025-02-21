import os
import telebot

# استبدل هذا بالتوكن الخاص بك
TOKEN = os.getenv("8120696288:AAHKAmbnqSvIi0-_9m0Shulm7Z0-bMbcvGU")
bot = telebot.TeleBot(TOKEN)

# دالة لمعالجة الأمر /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبًا! أنا بوت تيليغرام بسيط.")

# دالة لمعالجة الرسائل النصية
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

# بدء البوت
if __name__ == '__main__':
    bot.polling()
