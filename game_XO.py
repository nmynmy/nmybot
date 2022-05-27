from keyboa import Keyboa, Button
import random
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
users = {}
def generate_menu(button_list):
    keyboard = Keyboa(items=button_list, copy_text_to_callback=True, items_in_row=3)
    return keyboard()

def generate_board(call):
    matrix = users[call.from_user.id]['matrix']
    print(matrix)
    convert_matrix = [('❌' if i == 1 else '⭕') if i != 2 else '⬜' for i in matrix]
    users[call.from_user.id]['convert_matrix'] = convert_matrix
    board =dict(zip(range(9),convert_matrix))
    board_keys = [Button(button_data={'text': board[key], 'callback_data': str(key)}).button for key in board]
    return board_keys
def check_games(call):
    users[call.from_user.id]['search_game'] = True
    buffer_user = []
    for user in users:
        buffer_user.append(user)
        if len(buffer_user) == 2:
            users[buffer_user[0]]["oppo"] = buffer_user[1]
            users[buffer_user[1]]["oppo"] = buffer_user[0]
            buffer_user[0]['search_game'] = False
            buffer_user[1]['search_game'] = False

def check_win(call):
    board = users[call.from_user.id]['matrix']
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] and users[call.from_user.id]['step'] >= 3:
            print(board[each[0]],board[each[1]],board[each[2]])
            return "Победа"
    if users[call.from_user.id]['step'] == 9:
        return "Ничья"
    else:
        return False

def bot_recursiv(call):
    if users[call.from_user.id]['side'] == 1:
        cp_side=0
    else:
        cp_side=1
    board = users[call.from_user.id]['matrix']
    for each in win_coord:
        if board[each[0]] == board[each[1]] and board[each[2]] == 2:
            users[call.from_user.id]['matrix'][each[2]] = cp_side
            break
