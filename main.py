#Телеграм-бот от Григория Чахова(1-МД-15) :)

import telebot
from game_XO import *
from FUN import *
from SECRET import *
import DZ

import telebot
from telebot import types

from time import sleep

import BotGames
from menuBot import Menu, Users


bot = telebot.TeleBot(TOKEN)
game21 = None

@bot.message_handler(commands="start")
def command(message):
    chat_id = message.chat.id
    txt_message = f"Привет, {message.from_user.first_name}! Я тестовый бот Григория на языке Python"
    bot.send_sticker(chat_id, 'CAACAgIAAxkBAAITEWKZQX8UnFswPq4g8s4IfHuTTsGhAALXGAACbibhSwVjLcKY6_yrJAQ')
    bot.send_message(chat_id, text=txt_message, reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)

@bot.message_handler(content_types=['sticker'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    sticker = message.sticker
    bot.send_message(message.chat.id, sticker)

@bot.message_handler(content_types=['audio'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    audio = message.audio
    bot.send_message(chat_id, audio)

@bot.message_handler(content_types=['voice'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    voice = message.voice
    bot.send_message(message.chat.id, voice)

@bot.message_handler(content_types=['photo'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    photo = message.photo
    bot.send_message(message.chat.id, photo)

@bot.message_handler(content_types=['video'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    video = message.video
    bot.send_message(message.chat.id, video)

@bot.message_handler(content_types=['document'])
def get_messages(message):
    chat_id = message.chat.id
    mime_type = message.document.mime_type
    bot.send_message(chat_id, "Это " + message.content_type + " (" + mime_type + ")")

    document = message.document
    bot.send_message(message.chat.id, document)
    if message.document.mime_type == "video/mp4":
        bot.send_message(message.chat.id, "This is a GIF!")

@bot.message_handler(content_types=['location'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    location = message.location
    bot.send_message(message.chat.id, location)

@bot.message_handler(content_types=['contact'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    contact = message.contact
    bot.send_message(message.chat.id, contact)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global game21

    chat_id = message.chat.id
    ms_text = message.text

    cur_user = Users.getUser(chat_id)
    if message.text == "Крестики-нолики":
        id = message.from_user.id
        side = "1" #одностороняя игра с ботом
        locals()[id] = Game(str(message.from_user.username), side, message.from_user.username) #создаём класс с игрой
        bot.send_message(message.from_user.id, "Попробуй выиграть этот искусственный интеллект",reply_markup=generate_menu(
            users[str(message.from_user.username)].generate_board_bot('10'))) #"10" - костыль
        users[message.from_user.username].bot_recursiv()

    if cur_user == None :
        cur_user = Users(chat_id, message.json["from"])

    result = goto_menu(chat_id, ms_text)
    if result :
        return

    cur_menu = Menu.getCurMenu(chat_id)
    if cur_menu != None and ms_text in cur_menu.buttons:
        cur_user.set_cur_menu(ms_text)

        if ms_text == "📚 Помощь":
            send_help(chat_id)

        elif ms_text == '🎮 Придумать ник':
            bot.send_message(chat_id, text=get_nickname())

        elif ms_text == '🐶 Прислать собаку':
            bot.send_photo(chat_id, photo=get_dogURL(), caption="Вот тебе собачка")

        elif ms_text == '😅 Прислать анекдот':
            bot.send_message(chat_id, text=get_anekdot())

        elif ms_text == '🎬 Прислать фильм':
            send_film(chat_id)

        elif ms_text == '🎮 Случайная игра':
            bot.send_message(chat_id, text=get_game())

        elif ms_text == "Угадай кто?":
            get_ManOrNot(chat_id)

        elif ms_text == "❌⭕ Мультиплеер":
            bot.send_message(chat_id, text="В диалоге с другом просто напиши - '@testnmy_bot'")
            img = open('xo.jpg', 'rb')
            bot.send_photo(chat_id, img)



        elif ms_text == "Карту!" :
            if game21 == None :
                goto_menu(chat_id, "⬅ Выход")
                return
            text_game = game21.get_cards(1)
            bot.send_media_group(chat_id, media=getMediaCards(game21))
            bot.send_message(chat_id, text=text_game)

        elif ms_text == "Стоп!":
            game21 = None
            goto_menu(chat_id, "⬅ Выход")
            return


        elif ms_text in BotGames.GameRPS.values :  # реализация игры Камень-ножницы-бумага
            bot.send_message(chat_id, text="Ждем противника...")
            for _ in range(5) :
                text_game = ""
                for user in Users.activeUsers.values() :
                    if cur_user.get_cur_enemy() :
                        user = cur_user.get_cur_enemy()
                    if user.id != cur_user.id and user.get_cur_menu() in BotGames.GameRPS.values :
                        user.set_cur_enemy(cur_user)
                        enemy_value = user.get_cur_menu()
                        bot.send_message(chat_id, text="Твой Противник - @{enemy}".format(enemy=user.userName))
                        gameRSP = BotGames.getGame(chat_id)
                        if gameRSP == None :  # если мы случайно попали в это меню, а объекта с игрой нет
                            goto_menu(chat_id, "Выход")
                            return
                        text_game = gameRSP.onlineRPS(ms_text, enemy_value)
                        bot.send_message(chat_id, text=text_game)
                        gameRSP.newGame()
                        break
                if text_game :
                    break
                sleep(1)
            if not text_game :
                bot.send_message(chat_id, text="Друган не найден :С")
            sleep(1)
            cur_user.set_cur_menu("")
            cur_user.set_cur_enemy("")


        elif ms_text == "Задание 1" :
            DZ.dz1(bot, chat_id)
        elif ms_text == "Задание 2" :
            DZ.dz2(bot, chat_id)
        elif ms_text == "Задание 3" :
            DZ.dz3(bot, chat_id)
        elif ms_text == "Задание 4,5" :
            DZ.dz45(bot, chat_id)
        elif ms_text == "Задание 6" :
            DZ.dz6(bot, chat_id)
        elif ms_text == "Задание 7.1" :
            DZ.dz7n(bot, chat_id)
        elif ms_text == "Задание 7.2":
            DZ.dz7a(bot, chat_id)
        elif ms_text == "Задание 8" :
            DZ.dz8(bot, chat_id)
        elif ms_text == "Задание 9.1" :
            DZ.dz91(bot, chat_id)
        elif ms_text == "Задание 9.2" :
            DZ.dz92(bot, chat_id)
        elif ms_text == "Задание 10" :
            DZ.dz10(bot, chat_id)

    else:
        bot.send_message(chat_id, text="Мне жаль, я не понимаю вашу команду:" + ms_text)
        goto_menu(chat_id, "Главное меню")


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    print(call)
    if call.data in [str(i) for i in range(9)]:
        try: #Попытка завести онлайн
            if not getattr(users[call.inline_message_id],str(call.from_user.id)[::-1]):
                bot.answer_callback_query(call.id, "ЖДИ СВОЕЙ ОЧЕРЕДИ!!!🤬😡🤬😡") #вспылвающее окно
            else:
                if not users[call.inline_message_id].check_win():
                    bot.edit_message_reply_markup(inline_message_id=call.inline_message_id, reply_markup=generate_menu(users[call.inline_message_id].generate_board(str(call.from_user.id),str(call.data))))
                    if users[call.inline_message_id].check_win():
                        bot.edit_message_text(
                            text=users[call.inline_message_id].check_win() + " " + call.from_user.username + " 🥳",
                            inline_message_id=call.inline_message_id)
                else:
                    bot.edit_message_text(text=users[call.inline_message_id].check_win() + " " + call.from_user.username+" 🥳", inline_message_id=call.inline_message_id)
        except: #играем с ботом

            if not users[call.from_user.username].check_win(): #проверяем доску
                bot.edit_message_reply_markup(call.from_user.id, call.message.id, reply_markup=generate_menu( #изменяем под новый ход
                    users[str(call.from_user.username)].generate_board_bot(call.data)))
                users[call.from_user.username].bot_recursiv()

                if users[call.from_user.username].check_win():
                    bot.edit_message_text(
                        users[call.from_user.username].check_win() + " " + call.from_user.username + " 🥳",
                        call.from_user.id, call.message.id)
            else:
                bot.edit_message_text(users[call.from_user.username].check_win() + " " + call.from_user.username + " 🥳", call.from_user.id, call.message.id)

    elif call.inline_message_id: #присваиваем команду
        side = call.data.replace("❌", "0").replace("⭕", "1") #x,o -> 0,1
        try:
            try:
                if getattr(users[call.inline_message_id],str(call.from_user.id)) != side: #вытаскиваем из экземпляра класса его атримут
                    bot.answer_callback_query(call.id, "Вы уже выбрали сторону") #вспылвающее окно
            except:

                users[call.inline_message_id].add_user(str(call.from_user.id), side)
                bot.edit_message_reply_markup(inline_message_id=call.inline_message_id, reply_markup=generate_menu(
                    users[str(call.inline_message_id)].generate_board(str(call.from_user.id), '10')))
        except:
            bot.edit_message_reply_markup(inline_message_id=call.inline_message_id, reply_markup=generate_menu(["⭕","❌"].pop(int(side))))
            create_class(call.inline_message_id,call,side)

def create_class(id,call,side): #создаем класс(в случае онлайна)
    locals()[id] = Game(str(call.from_user.id), side, call.inline_message_id)



def goto_menu(chat_id, name_menu):
    cur_menu = Menu.getCurMenu(chat_id)
    if name_menu == "⬅ Выход" and cur_menu != None and cur_menu.parent != None:
        target_menu = Menu.getMenu(chat_id, cur_menu.parent.name)
    else:
        target_menu = Menu.getMenu(chat_id, name_menu)

    if target_menu != None :
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)

        if target_menu.name == "Игра в 21":
            global game21
            game21 = BotGames.newGame(chat_id, BotGames.Game21())
            text_game = game21.get_cards(2)
            bot.send_media_group(chat_id, media=getMediaCards(game21))
            bot.send_message(chat_id, text=text_game)

        elif target_menu.name == "Камень, ножницы, бумага":
            gameRPS = BotGames.newGame(chat_id, BotGames.GameRPS())
            text_game = "<b>Победитель определяется по следующим правилам: </b>\n" \
                        "1. Камень > Ножницы\n" \
                        "2. Бумага > Камень\n" \
                        "3. Ножницы > Бумага"
            bot.send_photo(chat_id, photo="https://media.istockphoto.com/photos/rock-paper-scissors-game-set-picture-id162675736", caption=text_game,
                           parse_mode='HTML')
        return True
    else:
        return False


def getMediaCards(game21):
    medias = []
    for url in game21.arr_cards_URL :
        medias.append(types.InputMediaPhoto(url))
    return medias


def send_film(chat_id):
    film = get_randomFilm()
    info_str = f"<b>{film['Наименование']}</b>\n" \
               f"Год: {film['Год']}\n" \
               f"Страна: {film['Страна']}\n" \
               f"Жанр: {film['Жанр']}\n" \
               f"Продолжительность: {film['Продолжительность']}"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Трейлер", url=film["Трейлер_url"])
    btn2 = types.InlineKeyboardButton(text="СМОТРЕТЬ онлайн", url=film["Фильм_url"])
    markup.add(btn1, btn2)
    bot.send_photo(chat_id, photo=film['Обложка_url'], caption=info_str, parse_mode='HTML', reply_markup=markup)


@bot.inline_handler(func=lambda query: True)
def empty_query(query):
    hint = "Поиграй в меня"
    try:
        r = types.InlineQueryResultArticle(
                id='1',
                title='Крестики нолики онлайн',
                description=hint,
                input_message_content=types.InputTextMessageContent(
                message_text="Добро пожаловать на сервер шизофрения",
                ),reply_markup=generate_menu(["❌","⭕"])) #выбор команды

        bot.answer_inline_query(query.id, [r], cache_time=1)
    except Exception as e:
        print(e)


bot.polling(none_stop=True, interval=0)

print()
