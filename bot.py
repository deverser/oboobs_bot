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
keyboard = types.ReplyKeyboardMarkup(True, True, row_width=1)
btn_y = types.KeyboardButton('Да, мне уже есть 18!')
btn_n = types.KeyboardButton('Нет, я ещё слишком молод...')
keyboard.row(btn_y)
keyboard.row(btn_n)

@bot.message_handler(commands=["start"])
def user_age_check(message):
    """Проверка пользователя на совершеннолетие"""
    bot.send_message(message.chat.id, text='Вам уже исполнилось 18 лет?', reply_markup=keyboard)


# @bot.message_handler(content_types=["text"])
# def bot_response_user(message):
#     """Ответ юзеру при проверке на совершеннолетие"""
#     if message.text == 'Да, мне уже есть 18!':
#         bot.send_message(message.chat.id, text='Добро пожаловать! Вы можете пользоваться этим ботом :)')
#     if message.text == 'Нет, я ещё слишком молод...':
#         bot.send_message(message.chat.id, text='К сожалению вы не можете пользоваться моими услугами')
    # elif message.text != '/boobs':
    #     bot.send_message(message.chat.id, text='Я не понимаю вас. Нажмите /start и выберите ответ с помощью кнопок')


@bot.message_handler(commands=["boobs"])
def send_last_boobs(message):
    """Присылает пользователю самое свежее фото сисек с oboobs.ru"""
    media_url = ar.get_boobs_url()
    bot.send_photo(message.chat.id, media_url)


if __name__ == '__main__':
    bot.polling(none_stop=True)
