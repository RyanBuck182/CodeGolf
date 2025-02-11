# Example By: Mason Lee

import os


def printBoard(board: list[list[int]]):
    print(" | ".join([str(x) for x in board[0]]))
    print("--+---+--")
    print(" | ".join([str(x) for x in board[1]]))
    print("--+---+--")
    print(" | ".join([str(x) for x in board[2]]))


def isValidMove(board: list[list[int]], move: str):
    flattenedBoard = [piece for row in board for piece in row]
    return move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and move in map(str, flattenedBoard)


def makeMove(board: list[list[int]], player: str):
    while True:
        move = input(f"{player} Pick a move (1-9): ")
        # If the move is not valid
        if not isValidMove(board, move):
            print("Invalid move!")
            continue

        board[(int(move) - 1) // 3][(int(move) - 1) % 3] = player
        return board


def isWin(board):
    # Check all horizontal conditions
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return True

    # Check all vertical conditions
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return True

    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True


def swapPlayer(player):
    return "O" if player == "X" else "X"


def isDraw(board):
    flattenedBoard = [piece for row in board for piece in row]
    for i in range(1, 10):
        if i in flattenedBoard:
            return False

    return True


if __name__ == "__main__":
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    currentPlayer = "X"
    printBoard(board)
    while True:
        board = makeMove(board, currentPlayer)
        os.system('cls')
        printBoard(board)
        if isWin(board):
            print(f"{currentPlayer} wins!")
            break
        if isDraw(board):
            print(f"It's a draw!")
            break
        currentPlayer = swapPlayer(currentPlayer)

    """Strings:
    Invalid move!
    It's a draw!
    {currentPlayer} wins!"""
