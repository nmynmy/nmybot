import time

def dz1(bot, chat_id):
    name1 = inputBot(message, "Введите своё имя.")
    bot.send_message(chat_id, "Ваше имя: " + name1)

def dz2(bot, chat_id):
    age = inputBot(message, "Введите свой возраст.")
    bot.send_message(chat_id, "Вам " + age + " лет.")

def dz3(bot, chat_id):
    name1 = inputBot(message, "Введите своё имя.") * 5
    bot.send_message(chat_id, name1)

def dz45(bot, chat_id):
    username = inputBot(message, "Введите имя.")
    user_age = int(inputBot(message, "Введите возраст."))
    bot.send_message(chat_id, "Добрый день, " + username)
    if user_age < 7 :
        bot.send_message(chat_id, "Почему ты не в садике")
    elif (user_age > 7) and user_age < 18 :
        bot.send_message(chat_id, "Иди делай уроки <3")
    elif user_age > 17 and user_age :
        bot.send_message(chat_id, "Какого это жить в ваши " + str(user_age) + "?")

def dz6(bot, chat_id):
    username = inputBot(message, "Введите имя.")
    length = len(username)
    bot.send_message(chat_id, str(username[1 :length - 1 :]))
    bot.send_message(chat_id, str(username[: :-1]))
    bot.send_message(chat_id, str(username[-3 : :]))
    bot.send_message(chat_id, str(username[:5 :]))

def dz7(bot, chat_id):
    username = inputBot(message, "Введите ваше имя.")
    user_age = int(inputBot(message, "Введите возраст."))
    sum = ((user_age // 10) + (user_age % 10))
    pr = ((user_age // 10) * (user_age % 10))
    bot.send_message(chat_id, "Длина имени пользователя: " + str(len(username)))
    bot.send_message(chat_id, "Сумма = " + str(sum))
    bot.send_message(chat_id, "Произведение = " + str(pr))

def dz8(bot, chat_id):
    username = inputBot(message, "Введите ваше имя.")
    nameU = str(str.upper(username))
    nameL = str(str.lower(username))
    nameUL = nameU[0 :1 :] + nameL[1 : :]
    nameLU = nameL[0 :1 :] + nameU[1 : :]
    bot.send_message(chat_id, nameU)
    bot.send_message(chat_id, nameL)
    bot.send_message(chat_id, nameUL)
    bot.send_message(chat_id, nameLU)

def dz9(bot, chat_id):
    username = inputBot(message, "Введите ваше имя.")
    user_age = int(inputBot(message, "Введите возраст."))
    spaces = 0
    for i in range(0, len(username)) :
        if username[i] == ' ' :
            print('В имени есть пробел!')
            spaces += 1
            break
        else :
            spaces = 0
    if spaces == 0 :
        bot.send_message(chat_id, 'В имени нет ошибок')
    else :
        bot.send_message(chat_id, 'В имени есть ошибка.')
    if user_age > 150 or user_age < 0 :
        bot.send_message(chat_id, 'Ошибка, такого возраста не существует!')
    else :
        bot.send_message(chat_id, 'В возрасте нет ошибок')

def dz10(bot, chat_id):
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

#дописать

