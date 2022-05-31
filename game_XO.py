from keyboa import Keyboa, Button
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
users = {}

class User():
    def __init__(self, username, id):
        self.username = username
        self.side = 1
        self.turn = True
        users[id] = self

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
        setattr(self, user, side[::-1])
        self.usertuple += (user,)

    def generate_board(self,id,coord):
        print(self.matrix)
        setattr(self, str(id)[::-1], False)
        setattr(self, "".join([i if i != id else "" for i in self.usertuple])[::-1], True)
        self.step += 1
        if int(coord) < 9:
            self.matrix[int(coord)] = int(getattr(self, id))
        convert_matrix = [('❌' if i == 1 else '⭕') if i != 2 else '⬜' for i in self.matrix]
        board = dict(zip(range(9), convert_matrix))
        board_keys = [Button(button_data={'text': board[key], 'callback_data': str(key)}).button for key in board]
        return board_keys

    def generate_board_bot(self,coord):
        self.step += 1
        if int(coord) < 9:
            self.matrix[int(coord)] = 1
        convert_matrix = [('❌' if i == 1 else '⭕') if i != 2 else '⬜' for i in self.matrix]
        board = dict(zip(range(9), convert_matrix))
        board_keys = [Button(button_data={'text': board[key], 'callback_data': str(key)}).button for key in board]
        return board_keys

    def check_win(self):
        for each in win_coord:
            if all([self.matrix[each[i]] for i in range(0,2)]) and self.step >= 5:
                return "Победа"
        if self.step >= 9:
            return "Ничья"
        else:
            return False

    def bot_recursiv(self):
        for each in win_coord:
            if self.matrix[each[0]] == self.matrix[each[1]] and self.matrix[each[2]] == 2:
                self.matrix[each[2]] = 0
                break
            elif self.matrix[each[2]] == self.matrix[each[1]] and self.matrix[each[0]] == 2:
                self.matrix[each[0]] = 0
                break
            elif self.matrix[each[2]] == self.matrix[each[0]] and self.matrix[each[1]] == 2:
                self.matrix[each[1]] = 0
                break

def generate_menu(button_list):
    keyboard = Keyboa(items=button_list, copy_text_to_callback=True, items_in_row=3)
    return keyboard()


