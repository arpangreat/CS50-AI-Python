"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1

    if countX > countO:
        return O
    elif countX == countO:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allActions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                allActions.add((row, col))

    return allActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    row, col = action
    newBoard = copy.deepcopy(board)
    newBoard[row][col] = player(board)

    return newBoard


def rowCheck(board, player):
    for row in range(len(board)):
        if (
            board[row][0] == player
            and board[row][1] == player
            and board[row][2] == player
        ):
            return True

    return False


def colCheck(board, player):
    for col in range(len(board)):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True

    return False


def checkFirstDiagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1

    if count == 3:
        return True
    else:
        return False


def checkSecondDiagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1

    if count == 3:
        return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (
        rowCheck(board, X)
        or colCheck(board, X)
        or checkFirstDiagonal(board, X)
        or checkSecondDiagonal(board, X)
    ):
        return X
    elif (
        rowCheck(board, O)
        or colCheck(board, O)
        or checkFirstDiagonal(board, O)
        or checkSecondDiagonal(board, O)
    ):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maxValue(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v


def minValue(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        playz = []
        for action in actions(board):
            playz.append((minValue(result(board, action)), action))
        return sorted(playz, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        playz = []
        for action in actions(board):
            playz.append((maxValue(result(board, action)), action))
        return sorted(playz, key=lambda x: x[0], reverse=True)[0][1]
