# -*- coding: utf-8 -*-
import telebot as tb
import config


"""
При создании бота мы создадим файл config, в котором на данный момент будет записан наш токен бота,
полученный при регистрации бота в Телеграм у @BotFather. Его мы добавляем в качестве аргумента при создании 
экземпляра бота в строке ниже
""" 
bot = tb.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def user_age_check(message):
    """Проверка пользователя на совершеннолетие"""
    bot.send_message(message.chat.id, text='Вам уже исполнилось 18 лет?')


if __name__ == '__main__':
    bot.polling(none_stop=True)