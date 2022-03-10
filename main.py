import random
import time

import bs4
import json
import requests
import telebot
from telebot import types

#dadadada
#dad
bot = telebot.TeleBot('5205176408:AAEecSdYmlIEzCZeWXg_Phb-aACPrXK8rvo')

def inputBot(message, text):
    a = []
    def ret(message):
        a.clear()
        a.append(message.text)
        return False

    a.clear()
    mes = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, ret)
    while a == []:
        pass
    return a[0]

def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
        return array_anekdots[0]

def get_film():
    req_film = requests.get('https://randomfilm.ru/')
    soup = bs4.BeautifulSoup(req_film.text, "html.parser")
    result_find = soup.findAll('h2')
    return(result_find)

def get_nickname():
    array_names = []
    req_names = requests.get("https://ru.nickfinder.com")
    soup = bs4.BeautifulSoup(req_names.text, "html.parser")
    result_find = soup.findAll(class_='one_generated_variant vt_df_bg')
    for result in result_find:
        array_names.append(result.getText())
        return array_names[0]





@bot.message_handler(commands=["start"])

def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("📚 Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id, text = "Привет, {0.first_name}! Я тестовый бот Григория.".format(
        message.from_user), reply_markup=markup )

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == '⬅ Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🎲 Развлечения')
        btn2 = types.KeyboardButton('📷 Web-камера')
        btn3 = types.KeyboardButton('🔧   Управление')
        btn4 = types.KeyboardButton('🤔 Задачки')
        back = types.KeyboardButton('📚 Помощь')
        markup.add(btn1, btn2, btn3,btn4, back)
        bot.send_message(chat_id, text='Вы в Главном меню',
                         reply_markup=markup)

    elif ms_text == '🤔 Задачки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        z1 = types.KeyboardButton('Задание 1')
        z2 = types.KeyboardButton('Задание 2')
        z3 = types.KeyboardButton('Задание 3')
        z4 = types.KeyboardButton('Задание 4,5')
        z6 = types.KeyboardButton('Задание 6')
        z7 = types.KeyboardButton('Задание 7')
        z8 = types.KeyboardButton('Задание 8')
        z9 = types.KeyboardButton('Задание 9')
        z10 = types.KeyboardButton('Задание 10')
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(z1, z2, z3, z4, z6, z7, z8, z9,z10, back)
        bot.send_message(chat_id, text='🤔 Задачки', reply_markup=markup)

    elif ms_text == "Задание 1":
        key1 = types.InlineKeyboardMarkup()
        name1 = inputBot(message, "Введите своё имя.")
        bot.send_message(chat_id,"Ваше имя: "+ name1)
    elif ms_text == "Задание 2":
        age = inputBot(message, "Введите свой возраст.")
        bot.send_message(chat_id, "Вам " + age + " лет.")
    elif ms_text == "Задание 3":
        name1 = inputBot(message, "Введите своё имя.") * 5
        bot.send_message(chat_id, name1)
    elif ms_text == "Задание 4,5":
        username = inputBot(message, "Введите имя.")
        user_age = int(inputBot(message, "Введите возраст."))
        bot.send_message(chat_id, "Добрый день, "+username)
        if user_age < 7 :
            bot.send_message(chat_id, "Почему ты не в садике")
        elif (user_age > 7) and user_age < 18 :
            bot.send_message(chat_id, "Иди делай уроки <3")
        elif user_age > 17 and user_age :
            bot.send_message(chat_id, "Какого это жить в ваши " + str(user_age) + "?")
    elif ms_text == "Задание 6":
        username = inputBot(message, "Введите имя.")
        length = len(username)
        bot.send_message(chat_id, str(username[1 :length - 1 :]))
        bot.send_message(chat_id, str(username[: :-1]))
        bot.send_message(chat_id, str(username[-3 : :]))
        bot.send_message(chat_id, str(username[:5 :]))
    elif ms_text == "Задание 7":
        username = inputBot(message, "Введите ваше имя.")
        user_age = int(inputBot(message, "Введите возраст."))
        sum = ((user_age//10) + (user_age%10))
        pr = ((user_age // 10) * (user_age % 10))
        bot.send_message(chat_id, "Длина имени пользователя: " + str(len(username)))
        bot.send_message(chat_id, "Сумма = " + str(sum) )
        bot.send_message(chat_id, "Произведение = " + str(pr) )
    elif ms_text == "Задание 8":
        username = inputBot(message, "Введите ваше имя.")
        nameU = str(str.upper(username))
        nameL = str(str.lower(username))
        nameUL = nameU[0 :1 :] + nameL[1 : :]
        nameLU = nameL[0 :1 :] + nameU[1 : :]
        bot.send_message(chat_id, nameU)
        bot.send_message(chat_id, nameL)
        bot.send_message(chat_id, nameUL)
        bot.send_message(chat_id, nameLU)
    elif ms_text == "Задание 9":
        username = inputBot(message, "Введите ваше имя.")
        user_age = int(inputBot(message, "Введите возраст."))
        spaces = 0
        for i in range(0, len(username)) :
            if username[i] == ' ' :
                print('В имени есть пробел!')
                spaces += 1
                break
            else : spaces = 0
        if spaces == 0: bot.send_message(chat_id, 'В имени нет ошибок')
        else: bot.send_message(chat_id, 'В имени есть ошибка.')
        if user_age > 150 or user_age < 0 : bot.send_message(chat_id, 'Ошибка, такого возраста не существует!')
        else: bot.send_message(chat_id, 'В возрасте нет ошибок')
    elif ms_text == "Задание 10":
        bot.send_message(chat_id, 'Приветствую вас на шоу кто хочет стать миллионером!')
        time.sleep(2)
        bot.send_message(chat_id, 'Вопрос на миллион рублей:')
        time.sleep(2)
        bot.send_message(chat_id, '.')
        time.sleep(2)
        bot.send_message(chat_id, '..')
        time.sleep(2)
        bot.send_message(chat_id, '...')
        time.sleep(3)
        bot.send_message(chat_id, 'Сколько будет 2+2*2?')

        ans = int(inputBot(message, "Иии ваш ответ???"))

        if ans == 6 :
            time.sleep(2)
            bot.send_message(chat_id, '.')
            time.sleep(2)
            bot.send_message(chat_id, '..')
            time.sleep(2)
            bot.send_message(chat_id, '...')
            time.sleep(2)
            bot.send_message(chat_id, '🧠Вы ответили верно! Ваше IQ больше 10! Поздравляю!🧠')
        elif ans == 8 :
            time.sleep(2)
            bot.send_message(chat_id, '.')
            time.sleep(2)
            bot.send_message(chat_id, '..')
            time.sleep(2)
            bot.send_message(chat_id, '...')
            time.sleep(2)
            bot.send_message(chat_id, "❌🧠 0_0")
        else :
            time.sleep(2)
            bot.send_message(chat_id, '.')
            time.sleep(2)
            bot.send_message(chat_id, '..')
            time.sleep(2)
            bot.send_message(chat_id, '...')
            time.sleep(2)
            bot.send_message(chat_id, 'Поздравляем! Ошибка 🥲')

    elif ms_text == "🎲 Развлечения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🐶 Прислать собаку")
        dog = types.KeyboardButton("🐶 Прислать собаку 2")
        btn2 = types.KeyboardButton("😅 Прислать анекдот")
        btn3 = types.KeyboardButton("🎬 Прислать фильм")
        btn5 = types.KeyboardButton("🎮 Придумать ник")
        btn4 = types.KeyboardButton('🎮 Случайная игра')
        back = types.KeyboardButton("⬅ Вернуться в главное меню")
        markup.add(btn1, dog, btn2, btn3, btn4, btn5, back)
        bot.send_message(chat_id, text = '🎲Развлечения', reply_markup=markup)

    elif ms_text =="/dog" or ms_text == '🐶 Прислать собаку':
        key1 = types.InlineKeyboardMarkup()
        img1 = open('ph1.jpg', 'rb')
        img2 = open('ph2.jpg', 'rb')
        img3 = open('ph3.jpg', 'rb')
        rnd_img = random.randint(0,2)
        if rnd_img == 0:
            bot.send_photo(message.chat.id, img1, reply_markup=key1)
            bot.send_message(chat_id, text="Вам попалась собака-ковбой 🤠")
        if rnd_img == 1:
            bot.send_photo(message.chat.id, img2, reply_markup=key1)
            bot.send_message(chat_id, text="Вам попалась собака-зайчик 🐇")
        if rnd_img == 2:
            bot.send_photo(message.chat.id, img3, reply_markup=key1)
            bot.send_message(chat_id, text="Вам попалась собака-белка🐿")

    elif ms_text == '🐶 Прислать собаку 2' :
        contents = requests.get('https://random.dog/woof.json').json()
        urldog = contents['url']
        bot.send_photo(chat_id, photo=urldog, caption="Вот тебе собачка")


    elif ms_text == '🎮 Случайная игра':
        print()



    elif ms_text == "🎮 Придумать ник":
        bot.send_message(chat_id, text=get_nickname())

    elif ms_text == '😅 Прислать анекдот':
        bot.send_message(chat_id, text=get_anekdot())

    elif ms_text == '🎬 Прислать фильм':
        bot.send_message(chat_id, text=get_film())

    elif ms_text == '📷 Web-камера':
        bot.send_message(chat_id, text="Я немного не понимаю, зачем нам веб-камера в тг боте 😅")
    elif ms_text == "🔧   Управление":
        bot.send_message(chat_id, text="Всё работает исправно")
        time.sleep(2)
        bot.send_message(chat_id, text="Надеюсь... 🥲")
    elif ms_text == "📚 Помощь" or ms_text == "/help":
        bot.send_message(chat_id, "Автор: Григорий Чахов 😎")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору",
                                          url="https://instagram.com/dreamofgregory")
        key1.add(btn1)
        img = open('ph.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)
#    else:
#        bot.send_message(chat_id, text="Я тебя слышку!!! Ваше сообщение: " + ms_text)

bot.polling(none_stop=True, interval=0)
print()







