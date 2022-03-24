import json
from gettext import find
from io import BytesIO

import telebot
from telebot import types
import requests
import bs4
import random
import time

import BotGames
from menuBot import Menu
import DZ

bot = telebot.TeleBot('5205176408:AAEecSdYmlIEzCZeWXg_Phb-aACPrXK8rvo')
game21 = None

check = Menu

@bot.message_handler(commands="start")
def command(message, res=False) :
    txt_message = f"Привет, {message.from_user.first_name}! Я бот Григория на языке Python"
    bot.send_message(message.chat.id, text=message,
                     reply_markup=check.getMenu("Главное меню").markup)


@bot.message_handler(message=['text'])
def get_text_messages(message) :
    global game21

    chat_id = message.chat.id
    ms_text = message.text

    result = goto_menu(chat_id, ms_text)
    if result :
        return
    if Menu.cur_menu != None and ms_text in Menu.cur_menu.buttons :
        if ms_text == "📚 Помощь" or ms_text == "/help" :
            send_help(chat_id)
        elif ms_text == '🐶 Прислать собаку' or ms_text == "/dog" :
            bot.send_photo(chat_id, photo=get_dogURL(), caption="Вот тебе собачка")

        elif ms_text == '😅 Прислать анекдот' :
            bot.send_message(chat_id, text= get_anekdot())

        elif ms_text == '🎬 Прислать фильм' :
            send_film(chat_id)

        elif ms_text == "Карту!" :
            if game21 == None :
                goto_menu(chat_id, "⬅ Выход")
                return
            text_game = game21.get_cards(1)
            bot.send_media_group(chat_id, media=getMediaCards(game21))
            bot.send_message(chat_id, text=text_game)

        elif ms_text == "Стоп!" :
            game21 = None
            goto_menu(chat_id, "⬅ Выход")
            return

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
        elif ms_text == "Задание 7" :
            DZ.dz7(bot, chat_id)
        elif ms_text == "Задание 8" :
            DZ.dz8(bot, chat_id)
        elif ms_text == "Задание 9" :
            DZ.dz9(bot, chat_id)
        elif ms_text == "Задание 10" :
            DZ.dz10(bot, chat_id)

        #####################################Дописываю всё остальное блин

        bot.send_message(chat_id, text="Мне жаль, я не понимаю вашу команду:" + ms_text)
        goto_menu(chat_id, "Главное меню")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    pass
    if call.data == "ManorNot_GoToSite":
        bot.answer_callback_query(call.id)








def goto_menu(chat_id, name_menu) :
    if name_menu == "⬅ Выход" and Menu.cur_menu != None and Menu.cur_menu.parent != None :
        target_menu = Menu.getMenu(Menu.cur_menu.parent.name)
    else :
        target_menu = Menu.getMenu(name_menu)

    if target_menu != None :
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)

        if target_menu.name == "Игра в 21" :
            global game21
            game21 = BotGames.Game21()
            text_game = game21.get_cards(2)
            bot.send_media_group(chat_id, media=getMediaCards(game21))
            bot.send_message(chat_id, text=text_game)

        return True
    else :
        return False


def getMediaCards(game21) :
    medias = []
    for url in game21.arr_cards_URL :
        medias.append(types.InputMediaPhoto(url))
    return medias


def send_help(chat_id) :
    global bot
    bot.send_message(chat_id, "Автор: Григорий Чахов 😎")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Напишите автору",
                                      url="https://instagram.com/dreamofgregory")
    markup.add(btn1)
    img = open('ph.jpg', 'rb')
    bot.send_photo(chat_id, img, reply_markup=markup)


def send_film(chat_id) :
    film = get_randomFilm()
    info_str = f'<b>{film["Наименование"]}<b>\n' \
               f'Год: {film["Год"]}\n' \
               f"Страна: {film['Страна']}\n" \
               f"Жанр: {film['Жанр']}\n" \
               f"Продолжительность: {film['Продолжительность']}"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Трейлер", utl=film["Трейлер_url"])
    btn2 = types.InlineKeyboardButton(text="Смотреть онлайн", url=film["Фильм_url"])
    markup.add(btn1, btn2)
    bot.send_photo(chat_id, photo=film['Обложка_url'], caption=info_str, parse_mode='HTML',
                   reply_markup=markup)


def get_randomFilm() :
    url = 'https://randomfilm.ru/'
    infoFilm = {}
    req_film = requests.get(url)
    soup = bs4.BeautifulSoup(req_film.text, "html.parser")
    result_find = soup.find('div', align="center", style="width: 100%")
    infoFilm["Наименование"] = result_find.find("h2").getText()
    names = infoFilm["Наименование"].split(" / ")
    infoFilm["Наименование_rus"] = names[0].strip()
    if len(names) > 1 :
        infoFilm["Наименование_eng"] = names[1].strip()

    images = []
    for img in result_find.findAll('img') :
        images.append(url + img.get('src'))
    infoFilm["Обложка_url"] = images[0]
    details = result_find.findAll('td')
    infoFilm["Год"] = details[0].contents[1].strip()
    infoFilm["Страна"] = details[1].contents[1].strip()
    infoFilm["Жанр"] = details[2].contents[1].strip()
    infoFilm["Продолжительность"] = details[3].contents[1].strip()
    infoFilm["Режиссёр"] = details[4].contents[1].strip()
    infoFilm["Актёры"] = details[5].contents[1].strip()
    infoFilm["Трейлер_url"] = url + details[6].contents[0]["href"]
    infoFilm["Актёры"] = details[7].contents[0]["href"]
    return infoFilm


def get_anekdot() :
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    if req_anek.status_code == 200 :
        soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
        result_find = soup.select('.anekdot_text')
        for result in result_find :
            array_anekdots.append(result.getText().strip())
    if len(array_anekdots) > 0 :
        return array_anekdots[0]
    else :
        return ""

def get_ManOrNot(chat_id):
    global bot

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Проверить",
                                      url="https://vc.ru/dev/58543-thispersondoesnotexist-sayt-generator-realistichnyh-lic")
    markup.add(btn1)

    req = requests.get("https://thispersondoesnotexist.com/image", allow_redirects=True)
    if req.status_code == 200:
        img = BytesIO(req.content)
        bot.send_photo(chat_id, photo=img, reply_markup=markup, caption="Этот человек реален?")







def get_dogURL() :
    url = ""
    req = requests.get('https://random.dog/woof.json')
    if req.status_code == 200 :
        r_json = req.json()
        url = r_json["url"]
    return url


bot.polling(none_stop=True, interval=0)

print("Кидаю step, лечу прям вверх")
