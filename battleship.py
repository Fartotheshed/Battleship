from random import randint

board = [["O"]*5 for i in range(5)]

def print_board(board):
    for row in board:
        print("".join(row))

print("Let's play!")
print_board(board)


ship_row = randint(0, len(board)-1)
ship_column = randint(0, len(board[0])-1)

for turn in range(4):
    guess_row = int(input("Guess the row:"))
    guess_column = int(input("Guess the column:"))

    if guess_row==ship_row and guess_column==ship_column:
        print("Target hit")
        break

    else:
        if guess_row < 0 or guess_column < 0 or guess_row > 4 or guess_column > 4:
            print("Not in the ocean!")
        elif board[guess_row][guess_column]=="X":
            print("Already picked")
        else:
            print("Target missed!")
            board[guess_row][guess_column]="X"
    if turn==3:
        print("Game finished")
    print_board(board)
