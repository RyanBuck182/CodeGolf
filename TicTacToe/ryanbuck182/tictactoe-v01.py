import os

n="\n"
DIVIDER=n+"--+---+--"+n
DIVIDER2JOIN=" | ".join

player = 'o'
winner=''

board = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

while 1:
    print(DIVIDER2JOIN(board[:3]) + DIVIDER + DIVIDER2JOIN(board[3:6]) + DIVIDER + DIVIDER2JOIN(board[6:]))
    if board[0:3].count(board[0]) == 3:break
    elif board[3:6].count(board[3]) == 3:break
    elif board[3:6].count(board[3]) == 3:break
    elif board[0::3].count(board[0]) == 3:break
    elif board[1::3].count(board[0]) ==3:break
    elif board[2::3].count(board[0]) ==3:break
    elif board[0::4].count(board[0]) ==3:break
    elif board[2::2].count(board[2]) ==3:break
    elif {*board}=={'x','o'}: player='d';break

    player = 'o' if player=='x' else 'x'
    move=''
    while 1:
        move = input(player+" Pick a move (1-9): ")
        if move.isnumeric() and move in board: break
        else: print("Invalid move!")
    board[int(move)-1] = player
    os.system('cls')

# print("It's a draw!") if player=='d' else print(player+" wins!")
if player=='d': print("It's a draw!")
else: print(player+" wins!")