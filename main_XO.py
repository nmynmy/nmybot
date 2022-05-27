import telebot
from game_XO import *
from telebot import types
import random

TOKEN = "5424381811:AAGtPI_Pni16IYb_MPJrTam2kw4E0a4LROg"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) #Начальный выбор
def start_menu(message):
    button_list = ["Сыграть с ботом","Найти игру"]
    bot.send_message(message.from_user.id, "выбери категорию", reply_markup=generate_menu(button_list))
    bot.delete_message(message.chat.id, message.message_id)
    users.update({message.from_user.id: {'matrix': [2] * 9, 'side': 1, 'step': 0 ,'oppo': None}})


    @bot.callback_query_handler(func=lambda call: True)
    def call_back(call):
        if call.data == "Найти игру": #Мультиплеер
            check_games(call)
            if users[call.from_user.id]['oppo'] is not None:

                bot.send_message(call.message.chat.id, "играй че ты а ?", reply_markup=generate_menu(generate_board(call)))

        elif call.data == "Сыграть с ботом":  #Синглплеер
            bot.send_message(call.message.chat.id, "Ты играешь за ❌")
            bot.send_message(call.message.chat.id, "Бот играет за ⭕")
            bot.send_message(call.message.chat.id, "играй че ты а ?", reply_markup=generate_menu(generate_board(call)))

        elif call.data in [str(i) for i in range(9)]:
            coordinate = int(call.data)
            new_matrix = users[call.from_user.id]['matrix']
            new_matrix[coordinate] = users[call.from_user.id]['side']
            users[call.from_user.id]['matrix'] = new_matrix
            print(users[call.from_user.id]['matrix'])
            users[call.from_user.id]['step'] += 1
            bot_recursiv(call)
            check = check_win(call)
            if not check:
                bot.send_message(call.message.chat.id, "играй че ты а ?", reply_markup=generate_menu(generate_board(call)))
            else:
                bot.send_message(call.message.chat.id, check)

        bot.delete_message(call.message.chat.id, call.message.message_id)

bot.infinity_polling()