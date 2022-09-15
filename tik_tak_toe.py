import random

def display_board(board):
    print("+-------" * 3, "+", sep='')

    for row in range(3):
        print("|       " * 3 + "|")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end='')
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3, "+", sep='')


def free_filds(board):
    free_feilds = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free_feilds.append((row, col))

    return free_feilds


def human_move(board):
    turn = True
    free_fields = free_filds(board)

    while turn:
        move = input("Enter Your Move: ")

        if not move.isdigit():
            print("Invalid Input! Enter a number between 1 to 9 corresponding to the Board")
        elif int(move) >= 1 and int(move) <= 9:
            move = int(move) - 1
            row = move // 3
            col = move % 3

            if (row, col) in free_fields:
                board[row][col] = "O"
                turn = False
            else:
                print("Wrong Move! The Box is already occupied")
        else:
            print("Invalid Input! Enter a number between 1 to 9 corresponding to the Board")


def computer_move(board):
    free_feilds = free_filds(board)
    
    while True:
        move = random.randint(0, 8)
        row = move // 3                           # for Computer move we've not used any formality. It'll move at core level 😎
        col = move % 3

        if (row, col) in free_feilds:
            board[row][col] = "X"
            return


def winner_analyzer_unit(board, sign):
    if sign == "X":
        who = "me"
    elif sign == "O":
        who = "you"
    else:
        who = None

    diag1 = True
    diag2 = True

    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:           # {board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign} same thing🤪,just tired to make little bit shorter😎 
            return who 
        if board[rc][rc] != sign:
            diag1 = False           
        if board[rc][2 - rc] != sign:
            diag2 = False

    if diag1 or diag2:
        return who
    return None


board = [[(3 * i + j + 1) for j in range(3)] for i in range(3)]
board[1][1] = "X"

free = free_filds(board)
human_turn = True

while len(free):
    display_board(board)

    if human_turn:
        print("\nHuman Turn...")
        human_move(board)
        win = winner_analyzer_unit(board, "O")
    else: 
        print("\nComputer Turn...")
        computer_move(board)
        win = winner_analyzer_unit(board, "X")

    if win != None:
        break

    human_turn = not human_turn    
    free = free_filds(board)

display_board(board)
if win == 'you':
	print("\nYou win!")
elif win == 'me':
	print("\nComputer win!")
else:
	print("\nTie!")                 # here, will come "Tie!" , check it out at the above ;D





































































# Mega approach of the Board :)

# for i in range(3):
#     new = []
#     for j in range(3):
#         bit = 3 * i + j + 1
#         new.append(bit)
#     board.append(new)

# print(board)


