# -*- coding: utf-8 -*-
import telebot as tb
from telebot import types
import config
import api_requests as ar


"""
При создании бота мы создадим файл config, в котором на данный момент будет записан наш токен бота,
полученный при регистрации бота в Телеграм у @BotFather. Его мы добавляем в качестве аргумента при создании 
экземпляра бота в строке ниже
""" 
bot = tb.TeleBot(config.token)
options_list = '/boobs - Присылает последнее фото сисек с сайта\n /random - Присылает рандомное фото сисек'


@bot.message_handler(commands=["help", "start"])
def show_bot_options(message):
    """Выводит инструкцию по всем командам бота"""
    bot.send_message(message.chat.id, text=options_list)


@bot.message_handler(commands=["boobs"])
def send_last_boobs(message):
    """Присылает пользователю самое свежее фото сисек с oboobs.ru"""
    media_url = ar.get_boobs_url()
    bot.send_photo(message.chat.id, media_url)


@bot.message_handler(commands=["random"])
def send_random_boobs(message):
    """Присылает пользователю рандомное фото сисек"""
    media_url = ar.get_random_boobs()
    bot.send_photo(message.chat.id, media_url)


if __name__ == '__main__':
    bot.polling(none_stop=True)
