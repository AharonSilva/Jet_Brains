enter = '_________'
enter = enter.replace("_", " ")
enter = list(enter)

board = [
    [enter[0], enter[1], enter[2]],
    [enter[3], enter[4], enter[5]],
    [enter[6], enter[7], enter[8]]
]

board2 = [
    [enter[6], enter[3], enter[0]],
    [enter[7], enter[4], enter[1]],
    [enter[8], enter[5], enter[2]],
]


def board_display():
    print("---------")
    print("|", board[0][0],  board[0][1], board[0][2], "|")
    print("|", board[1][0],  board[1][1], board[1][2], "|")
    print("|", board[2][0],  board[2][1], board[2][2], "|")
    print("---------")

# Checking winner by row:
    if (board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == 'X'):
        print('X wins')
        exit()
    elif (board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == 'X'):
        print('X wins')
        exit()
    elif (board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == 'X'):
        print('X wins')
        exit()
    elif (board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == 'O'):
        print('O wins')
        exit()
    elif (board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == 'O'):
        print('O wins')
        exit()
    elif (board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == 'O'):
        print('O wins')
        exit()

# Checking winner by column:
    if (board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == 'X'):
        print('X wins')
        exit()
    elif (board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == 'X'):
        print('X wins')
        exit()
    elif (board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == 'X'):
        print('X wins')
        exit()
    elif (board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == 'O'):
        print('O wins')
        exit()
    elif (board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == 'O'):
        print('O wins')
        exit()
    elif (board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == 'O'):
        print('O wins')
        exit()

# Checking winner in diagonals:
    if (board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == 'X'):
        print('X wins')
        exit()
    elif (board[0][2] == 'X') and (board[1][1] == 'X') and (board[2][0] == 'X'):
        print('X wins')
        exit()
    elif (board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == 'O'):
        print('O wins')
        exit()
    elif (board[0][2] == 'O') and (board[1][1] == 'O') and (board[2][0] == 'O'):
        print('O wins')
        exit()

# Checking if draw:
    if (sum(' ' in sublist for sublist in board)) == 0:
        print('Draw')
        exit()


def player_x():

    while True:
        move = input("Enter the coordinates:")
        coords = move.split(" ")
        if coords[0].isalpha() or coords[1].isalpha():
            print("You should enter numbers!")
        elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
            print("Coordinates should be from 1 to 3!")
        elif board[(int(coords[1]) - 3) * -1][int(coords[0]) - 1] == 'X' or \
                board[(int(coords[1]) - 3) * -1][int(coords[0]) - 1] == 'O':
            print("This cell is occupied! Choose another one!")
        else:
            if int(coords[0]) == 1 and int(coords[1]) == 1:
                board[2][0] = "X"
            if int(coords[0]) == 1 and int(coords[1]) == 2:
                board[1][0] = "X"
            if int(coords[0]) == 1 and int(coords[1]) == 3:
                board[0][0] = "X"
            if int(coords[0]) == 2 and int(coords[1]) == 1:
                board[2][1] = "X"
            if int(coords[0]) == 2 and int(coords[1]) == 2:
                board[1][1] = "X"
            if int(coords[0]) == 2 and int(coords[1]) == 3:
                board[0][1] = "X"
            if int(coords[0]) == 3 and int(coords[1]) == 1:
                board[2][2] = "X"
            if int(coords[0]) == 3 and int(coords[1]) == 2:
                board[1][2] = "X"
            if int(coords[0]) == 3 and int(coords[1]) == 3:
                board[0][2] = "X"
            board_display()
            break


def player_o():
    while True:
        move = input("Enter the coordinates:")
        coords = move.split(" ")
        if coords[0].isalpha() or coords[1].isalpha():
            print("You should enter numbers!")
        elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
            print("Coordinates should be from 1 to 3!")
        elif board[(int(coords[1]) - 3) * -1][int(coords[0]) - 1] == 'X' or \
                board[(int(coords[1]) - 3) * -1][int(coords[0]) - 1] == 'O':
            print("This cell is occupied! Choose another one!")
        else:
            if int(coords[0]) == 1 and int(coords[1]) == 1:
                board[2][0] = "O"
            if int(coords[0]) == 1 and int(coords[1]) == 2:
                board[1][0] = "O"
            if int(coords[0]) == 1 and int(coords[1]) == 3:
                board[0][0] = "O"
            if int(coords[0]) == 2 and int(coords[1]) == 1:
                board[2][1] = "O"
            if int(coords[0]) == 2 and int(coords[1]) == 2:
                board[1][1] = "O"
            if int(coords[0]) == 2 and int(coords[1]) == 3:
                board[0][1] = "O"
            if int(coords[0]) == 3 and int(coords[1]) == 1:
                board[2][2] = "O"
            if int(coords[0]) == 3 and int(coords[1]) == 2:
                board[1][2] = "O"
            if int(coords[0]) == 3 and int(coords[1]) == 3:
                board[0][2] = "O"
            board_display()
            break

board_display()
while True:
    player_x()
    player_o()

