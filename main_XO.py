import telebot
from game_XO import *
from telebot import  types
import random
TOKEN = "5547975470:AAH1j119wcJYAEJOMPZosSmmJenqXMpRAfU"
msg = {}
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_menu(message):
    button_list =["Сыграть с ботом"]
    bot.send_message(message.from_user.id, "выбери категорию", reply_markup=generate_menu(button_list))
    bot.delete_message(message.chat.id, message.message_id)
    users.update({message.from_user.id: {'matrix': [2] * 9, 'side': 1, 'step':0,'oppo': None}})

@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    print(call)
    if call.data == "Сыграть с ботом":
        id = call.from_user.id
        side = "1"
        locals()[id] = Game(str(call.from_user.username), side, call.from_user.username)
        bot.edit_message_reply_markup(call.from_user.id, call.message.id,reply_markup=generate_menu(
            users[str(call.from_user.username)].generate_board_bot('10')))
    if call.data in [str(i) for i in range(9)]:
        try:

            if not getattr(users[call.inline_message_id],str(call.from_user.id)[::-1]):
                bot.answer_callback_query(call.id, "ЖДИ СВОЕЙ ОЧЕРЕДИ!!!🤬😡🤬😡")
            else:
                if not users[call.inline_message_id].check_win():
                    bot.edit_message_reply_markup(inline_message_id=call.inline_message_id, reply_markup=generate_menu(users[call.inline_message_id].generate_board(str(call.from_user.id),str(call.data))))
                else:
                    bot.edit_message_text(text=users[call.inline_message_id].check_win() + " " + call.from_user.username+"`a🥳", inline_message_id=call.inline_message_id)
        except:
            if not users[call.from_user.username].check_win():
                bot.edit_message_reply_markup(call.from_user.id, call.message.id, reply_markup=generate_menu(
                    users[str(call.from_user.username)].generate_board_bot(call.data)))
                users[call.from_user.username].bot_recursiv()
            else:
                bot.edit_message_text(call.from_user.id, call.message.id,
                                      users[call.from_user.username].check_win() + " " + call.from_user.username + "`a🥳")
    elif call.inline_message_id:
        side = call.data.replace("❌", "0").replace("⭕", "1")
        print(side)
        try:
            try:
                if getattr(users[call.inline_message_id],str(call.from_user.id)) != side:
                    bot.answer_callback_query(call.id, "вы уже выбрали сторону")
            except:
                users[call.inline_message_id].add_user(str(call.from_user.id), side)
                bot.edit_message_reply_markup(inline_message_id=call.inline_message_id, reply_markup=generate_menu(
                    users[str(call.inline_message_id)].generate_board(str(call.from_user.id), '10')))
        except:
            bot.edit_message_reply_markup(inline_message_id=call.inline_message_id, reply_markup=generate_menu(["⭕","❌"].pop(int(side))))
            create_class(call.inline_message_id,call,side)



def create_class(id,call,side):
    locals()[id] = Game(str(call.from_user.id), side, call.inline_message_id)
@bot.inline_handler(func=lambda query: True)
def empty_query(query):
    print(query)
    users.update({query.from_user.id: {'matrix': [2] * 9, 'side': 1, 'step': 0, 'chat': query}})
    hint = "Введите ровно 2 числа и получите результат!"
    try:
        r = types.InlineQueryResultArticle(
                id='1',
                title='fdfdf',
                description=hint,
                input_message_content=types.InputTextMessageContent(
                message_text="Эх, зря я не ввёл 2 числа :(",
                ),reply_markup=generate_menu(["❌","⭕"]))
        bot.answer_inline_query(query.id, [r])
        msg[query.from_user.id] = query.id
    except Exception as e:
        print(e)
bot.infinity_polling()
