from telebot import types


class Menu:
    hash = {}
    cur_menu = None
    extendedParameters = {}

    def __init__(self, name, buttons=None, parent=None, action=None):
        self.parent = parent
        self.name = name
        self.buttons = buttons
        self.action = action

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        markup.add(*buttons)
        self.markup = markup
        self.__class__.hash[name] = self

    @classmethod
    def getExrPar(cls, id):
        return cls.extendedParameters.pop(id, None)

    @classmethod
    def setExtPar(cls, parameter):
        import uuid
        id = uuid.uuid4().hex
        cls.extendedParameters[id] = parameter
        return id

    @classmethod
    def getMenu(cls, name):
        menu = cls.hash.get(name)
        if menu != None :
            cls.cur_menu = menu
        return menu


m_main = Menu("Главное меню", buttons=["🎲 Развлечения", "🕹️ Игры", '🤔 Задачки', "📚 Помощь"])

m_games = Menu("🕹️ Игры", buttons=["Камень, ножницы, бумага", "Игра в 21", "Угадай кто?",
                                    "⬅ Выход"], parent=m_main)
m_game_21 = Menu("Игра в 21", buttons=["Карту!", "Стоп!", "⬅ Выход"],
                 parent=m_games, action="game21")
m_game_rsp = Menu("Камень, ножницы, бумага", buttons=["Камень!", "Ножницы!", "Бумага!",
                                                      "⬅ Выход"], parent=m_games, action="game_rsp")
m_DZ = Menu("🤔 Задачки", buttons=["Задание 1", 'Задание 2', 'Задание 3', 'Задание 4,5', 'Задание 6', 'Задание 7',
                                   'Задание 8', 'Задание 9', 'Задание 10', "⬅ Выход"], parent=m_main)
m_fun = Menu("🎲 Развлечения", buttons=["🐶 Прислать собаку", "😅 Прислать анекдот", "🎬 Прислать фильм",
                                        "🎮 Придумать ник", "🎮 Случайная игра", "⬅ Выход"], parent=m_main)
