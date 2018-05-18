# -*- coding: utf-8 -*-
from telebot import apihelper
from telebot import util
from telebot import types
import config
import telebot
import os, time

apihelper.proxy = {'https':'socks5://503533686:zfC80WpU@185.211.245.142:1090'}

bot = telebot.TeleBot(config.token)
def largeTextFileSender(file, chat_id):
    largeText = open(file, "rb").read()
    splitted_text = util.split_string(largeText, 3000)
    for text in splitted_text:
        bot.send_message(chat_id, text)

@bot.message_handler(commands=['start'])
def welcomeMessage(message):
    largeTextFileSender(file='hello.txt', chat_id=message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('/Температура')
    itembtn2 = types.KeyboardButton('/Таймеры')
    itembtn3 = types.KeyboardButton('/Кондей')

    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(commands=['Температура'])
def welcomeMessage(message):
    text = 'Температура внутри: '
    text += '+25C'
    bot.send_message(message.chat.id, text)
    print (text)

@bot.message_handler(commands=['help'])
def helpMessage(message):
    largeTextFileSender(file='help.txt', chat_id=message.chat.id)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)

if __name__ == '__main__':
    bot.polling(none_stop=True)