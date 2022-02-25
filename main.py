import telebot
from telebot import types
#dadadada

bot = telebot.TeleBot('5205176408:AAEecSdYmlIEzCZeWXg_Phb-aACPrXK8rvo')

@bot.message_handler(commands=["start"])

def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id, text = "Привет, {0.first_name}! Я тестовый бот Григория.".format(
        message.from_user), reply_markup=markup )

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🎲Развлечения')
        btn2 = types.KeyboardButton('Web-камера')
        btn3 = types.KeyboardButton('Управление')
        back = types.KeyboardButton('Помощь')
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text='Вы в Главном меню',
                         reply_markup=markup)
    elif ms_text == "🎲Развлечения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку🐶")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text = '🎲Развлечения', reply_markup=markup)

    elif ms_text =="/dog" or ms_text == 'Прислать собаку🐶':
        bot.send_message(chat_id, text="Еще не готово")
    elif ms_text == 'Прислать анекдот':
        bot.send_message(chat_id, text="Еще не готово")
    elif ms_text == 'Web-камера':
        bot.send_message(chat_id, text="Еще не готово")
    elif ms_text == "Управление":
        bot.send_message(chat_id, text="еще не готово")
    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, "Автор: Григорий Чахов")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору",
                                          url="https://instagram.com/dreamofgregory")
        key1.add(btn1)
        img = open('ph.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)
    else:
        bot.send_message(chat_id, text="Я тебя слышку!!! Ваше сообщение: " + ms_text)

bot.polling(none_stop=True, interval=0)
print()







