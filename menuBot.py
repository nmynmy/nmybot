from telebot import types

# -----------------------------------------------------------------------

class KeyboardButton:
    def __init__(self, name, handler=None):
        self.name = name
        self.handler = handler

# -----------------------------------------------------------------------

class Users:
    activeUsers = {}

    def __init__(self, chat_id, user_json):
        self.id = user_json["id"]
        self.isBot = user_json["is_bot"]
        self.firstName = user_json["first_name"]
        self.userName = user_json["username"]
        self.languageCode = user_json["language_code"]

        self.__class__.activeUsers[chat_id] = self

    def __str__(self):
        return f"Name user: {self.firstName}   id: {self.userName}   lang: {self.languageCode}"

    def getUserHTML(self):
        return f"Name user: {self.firstName}   id: <a href='https://t.me/{self.userName}'>{self.userName}</a>   lang: {self.languageCode}"


    @classmethod
    def getUser(cls, chat_id):
        return cls.activeUsers.get(chat_id)

# -----------------------------------------------------------------------

class Menu:
    hash = {}
    cur_menu = {}
    extendedParameters = {}


    def __init__(self, name, buttons=None, parent=None, handler=None):
        self.parent = parent
        self.name = name
        self.buttons = buttons
        self.handler = handler

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(*buttons)
        self.markup = markup

        self.__class__.hash[name] = self

    @classmethod
    def getExtPar(cls, id):
        return cls.extendedParameters.pop(id, None)

    @classmethod
    def setExtPar(cls, parameter):
        import uuid
        id = uuid.uuid4().hex
        cls.extendedParameters[id] = parameter
        return id

    @classmethod
    def getMenu(cls, chat_id, name):
        menu = cls.hash.get(name)
        if menu != None:
            cls.cur_menu[chat_id] = menu
        return menu

    @classmethod
    def getCurMenu(cls, chat_id):
        return cls.cur_menu.get(chat_id)

m_main = Menu("Главное меню", buttons=["🎲 Развлечения", "🕹️ Игры", '🤔 Задачки', "📚 Помощь"])

m_games = Menu("🕹️ Игры", buttons=["Камень, ножницы, бумага", "Игра в 21", "Угадай кто?",
                                    "⬅ Выход"], parent=m_main)
m_game_21 = Menu("Игра в 21", buttons=["Карту!", "Стоп!", "⬅ Выход"], parent=m_games, handler="game_21")

m_game_rsp = Menu("Камень, ножницы, бумага", buttons=["Камень", "Ножницы", "Бумага", "⬅ Выход"], parent=m_games, handler="game_rsp")

m_DZ = Menu("🤔 Задачки", buttons=["Задание 1", 'Задание 2', 'Задание 3', 'Задание 4,5', 'Задание 6', 'Задание 7.1',
                                   'Задание 7.2', 'Задание 8', 'Задание 9.1', 'Задание 9.2', 'Задание 10', "⬅ Выход"], parent=m_main)
m_fun = Menu("🎲 Развлечения", buttons=["🐶 Прислать собаку", "😅 Прислать анекдот", "🎬 Прислать фильм",
                                        "🎮 Придумать ник", "🎮 Случайная игра", "⬅ Выход"], parent=m_main)