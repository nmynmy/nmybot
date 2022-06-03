from keyboa import Keyboa, Button
import random

win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) #координаты победы
users = {}

class Game:
    def __init__(self, user, side, name):
        self.matrix = [2] * 9
        self.step = 0
        self.usertuple = (user,)
        setattr(self, user, [side,False])
        setattr(self, user, side[::-1])
        users[name] = self

    def add_user(self,user,side):
        setattr(self, user, side)
        setattr(self, user, side[::-1]) #
        self.usertuple += (user,)

    def generate_board(self,id,coord): #создание стола(хода)
        setattr(self, str(id)[::-1], False) #переворачиваем id, чтобы игроки не ходили в чужой ход
        setattr(self, "".join([i if i != id else "" for i in self.usertuple])[::-1], True) #Прогоняем котреж (1) если = то это тот юзер, который нам нужен (2) != если это не тот
        self.step += 1
        if int(coord) < 9:
            self.matrix[int(coord)] = int(getattr(self, id))
        convert_matrix = [('⭕' if i == 1 else '❌') if i != 2 else '⬜' for i in self.matrix]
        board = dict(zip(range(9), convert_matrix)) #склеиваем в новый словарик новый ход матрицы
        board_keys = [Button(button_data={'text': board[key], 'callback_data': str(key)}).button for key in board]
        return board_keys

    def generate_board_bot(self,coord):
        self.step += 1
        if int(coord) < 9:
            self.matrix[int(coord)] = 1
        convert_matrix = [('❌' if i == 1 else '⭕') if i != 2 else '⬜' for i in self.matrix] #конвертируем матрицу из 0,1,2 -> x,o и квадратик
        board = dict(zip(range(9), convert_matrix))
        board_keys = [Button(button_data={'text': board[key], 'callback_data': str(key)}).button for key in board] #генерируем кнопки в списке
        return board_keys

    def check_win(self):
        print(self.matrix)
        for each in win_coord:
            if self.matrix[each[0]] == self.matrix[each[1]] == self.matrix[each[2]] != 2:
                return "Победа"
        if self.step >= 9:
            return "Ничья"
        else:
            return False

    def bot_recursiv(self): #попытка создать ИИ не увенчалась успехом :(
        random_step = random.randint(0, 8)
        if self.matrix[random_step] == 2 :
            self.matrix[random_step] = 0
        else:
            self.bot_recursiv()


def generate_menu(button_list):
    keyboard = Keyboa(items=button_list, copy_text_to_callback=True, items_in_row=3)
    return keyboard()