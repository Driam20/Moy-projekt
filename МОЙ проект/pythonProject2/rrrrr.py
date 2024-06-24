import os
from random import randint

config = {
    "board_size": (3),

    "step_type": ("X", "0"),
    "player_type": ("I", "C"),
    "session_state": ("SE", "X", "0", "DRAW"),

    "cell_nums": list(range(10)),




    "player_step_type": None,
    "computer_step_type": None,

    "player_step_cell": None,
    "computer_step_cell": None,
    "first_step": None,
    "last_step": None,
    "break_session": False
}
board = []
print_data = []



def clear():
    os.system('cls')



def check_cell(cell_number):
    x = get_cell_coord(cell_number)
    return board[x[0]][x[1]]



def print_board():
    print('\033[2J')
    print("")
    print("\u001b[0m-------- Табло --------\u001b[38;5;4m")
    print(*print_data, sep="\n")
    print("\u001b[0m-------- Табло --------\u001b[0m")

    for i in range(1, len(board) + 1):
        for j in range(1, len(board) + 1):
            s = "\u001b[38;5;<brd_c>m(\u001b[38;5;<step_c>m<step_type>\u001b[38;5;<brd_c>m)\u001b[0m"
            s2 = str(board[i - 1][j - 1])

            s = s.replace("<step_type>", s2)

            if s2 == "X":
                s = s.replace("<step_c>", "14")
            elif s2 == "0":
                s = s.replace("<step_c>", "11")
            else:
                s = s.replace("<step_c>", "7")


            s = s.replace("<brd_c>", "8")
            print(s, end="")
        print("")



def init_board():
    z = [[" " for j in range(config["board_size"])] for i in range(config["board_size"])]
    for i in range(config["board_size"]**2):
        y = get_cell_coord(i + 1)
        z[y[0]][y[1]] = str(i + 1)
    return z



def ask_step_type():
    while True:
        s = str.upper(input(f"Выберите крестик или нолик ({', '.join(config['step_type'])}):"))
        if s not in config["step_type"]:
            print("Неверный выбор!")
        else:
            if s == config["step_type"][0]:
                config["player_step_type"] = 0
                config["computer_step_type"] = 1
            else:
                config["player_step_type"] = 1
                config["computer_step_type"] = 0
            print_data.append(f'Ваша фишка - "{config["step_type"][config["player_step_type"]]}"')
            print_data.append(f'Фишка компьютера - "{config["step_type"][config["computer_step_type"]]}"')
            break



def ask_human_first_step():
    while True:
        s = input('Кто будет ходить первым - вы или компьютер? Введите "I" или "C":').strip().upper()
        if s not in config["player_type"]:
            print("Ошибка!")
            continue
        config["first_step"] = config["player_type"].index(s)
        print_data.append(f'Первым ходит {"игрок" if s == config["player_type"][0] else "компьютер"}')
        break


def get_cell_coord(
        cell_num
                   ):
    if cell_num == 7:
        return 0, 0
    elif cell_num == 8:
        return 0, 1
    elif cell_num == 9:
        return 0, 2
    elif cell_num == 4:
        return 1, 0
    elif cell_num == 5:
        return 1, 1
    elif cell_num == 6:
        return 1, 2
    elif cell_num == 1:
        return 2, 0
    elif cell_num == 2:
        return 2, 1
    elif cell_num == 3:
        return 2, 2



def do_human_step():

    while True:
        s = input(f"Ваш ход (введите номер клетки, 0 - завершение игры): ")
        if not s.strip().isalnum():
            print("Ошибка! Нужно вводить только цифры!")
            continue
        z = int(s)
        if z not in config["cell_nums"]:
            print(f'Ошибка! Номер клетки должен быть от 1 до {len(config["cell_nums"]) - 1}')
            continue

        if z == 0:
            print(z)
            return -1

        x = get_cell_coord(z)
        if board[x[0]][x[1]] in config["step_type"]:
            print(f"Ошибка! Клетка номер {z} занята!")
            continue
        config["player_step_cell"] = z
        x = get_cell_coord(z)
        board[x[0]][x[1]] = config["step_type"][config["player_step_type"]]
        config["last_step"] = 0
        print_board()
        break
    return z



def analyze_board():

    x = check_lines()
    if x == "X":
        return config["session_state"][1]
    elif x == "0":
        return config["session_state"][2]


    free_cell_count = 0
    for i in range(config["board_size"]**2):
        y = get_cell_coord(i + 1)
        if not board[y[0]][y[1]].isalpha():
            if 1 <= int(board[y[0]][y[1]]) <= 9:
                free_cell_count += 1
    if not free_cell_count:
        return config["session_state"][3]

    return config["session_state"][0]



def check_lines():
    s = "X"

    if board[0][0] == s and board[0][1] == s and board[0][2] == s or \
        board[1][0] == s and board[1][1] == s and board[1][2] == s or \
        board[2][0] == s and board[2][1] == s and board[2][2] == s or \
        board[0][0] == s and board[1][0] == s and board[2][0] == s or \
        board[0][1] == s and board[1][1] == s and board[2][1] == s or \
        board[0][2] == s and board[1][2] == s and board[2][2] == s or \
        board[0][0] == s and board[1][1] == s and board[2][2] == s or \
        board[0][2] == s and board[1][1] == s and board[2][0] == s:
        return s
    s = "0"
    if board[0][0] == s and board[0][1] == s and board[0][2] == s or \
        board[1][0] == s and board[1][1] == s and board[1][2] == s or \
        board[2][0] == s and board[2][1] == s and board[2][2] == s or \
        board[0][0] == s and board[1][0] == s and board[2][0] == s or \
        board[0][1] == s and board[1][1] == s and board[2][1] == s or \
        board[0][2] == s and board[1][2] == s and board[2][2] == s or \
        board[0][0] == s and board[1][1] == s and board[2][2] == s or \
        board[0][2] == s and board[1][1] == s and board[2][0] == s:
        return s
    return ""


def do_comp_step():
    z = randint(1, config["board_size"]**2)
    while True:
        xx = check_cell(z)
        if xx in config["step_type"]:
            z = randint(1, config["board_size"] ** 2)
        else:
            break
    config["computer_step_cell"] = z
    x = get_cell_coord(z)
    board[x[0]][x[1]] = config["step_type"][config["computer_step_type"]]
    config["last_step"] = 1
    print_board()


def do_step():
    if config["last_step"] == 1:
        if do_human_step() == -1:
            config["break_session"] = True
    else:
        do_comp_step()



def session_state():
    x = analyze_board()



    if x == config["session_state"][1]:
        if config["player_step_type"] == 0:
            s = "Вы выиграли! :)))"
        else:
            s = "Вы проиграли! :((("
    elif x == config["session_state"][2]:
        if config["player_step_type"] == 1:
            s = "Вы выиграли! :)))"
        else:
            s = "Вы проиграли! :((("
    elif x == config["session_state"][3]:
        s = "Ничья! :|||"
    print("\u001b[38;5;9m" + s + "\u001b[0m")



board = init_board()

ask_step_type()
ask_human_first_step()
print_board()


sess_state = None
if config["first_step"] == 0:
    config["last_step"] = 1

while True:
    do_step()
    if config["break_session"]:
        session_state()
        break

    sess_state = analyze_board()

    if sess_state != config["session_state"][0]:
        session_state()
        break