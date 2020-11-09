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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    print("running player")
    Xcnt = 0
    Ocnt = 0
    if board == initial_state():
        return X

    for j in range(len(board[1])):
        for i in range(len(board)):
            if board[j][i] == X:
                Xcnt += 1
            if board[j][i] == O:
                Ocnt += 1

    if Xcnt == Ocnt:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    print("running actions")
    moves = []
    for r in range(len(board[0])):      # Rows
        for c in range(len(board)):     # Columns
            if board[r][c] == None:
                moves.append([r, c])
    #print(moves)
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print("running result")
    board_move = copy.deepcopy(board)
    if board_move[action[0]][action[1]] is None:
        board_move[action[0]][action[1]] = player(board)
        return board_move
    else:
        return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    print("running winner")

    # Rows
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    # Columns
    col1 = [board[0][0], board[1][0], board[2][0]]
    col2 = [board[0][1], board[1][1], board[2][1]]
    col3 = [board[0][2], board[1][2], board[2][2]]
    # Diag
    dia1 = [board[0][0], board[1][1], board[2][2]]
    dia2 = [board[0][2], board[1][1], board[2][0]]

    winner = [row1, row2, row3, col1, col2, col3, dia1, dia2]

    for l in winner:
        if all(x == l[0] for x in l):
            if l[0] is not None:
                print(l)
                print(winner)
                return l[0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    print("running terminal")
    if winner(board) != None:
        print("WINNER!!!")
        return True
    elif None not in board[0] and None not in board[1] and None not in board[2]:
        print("No Available Spaces")
        return True
    elif None in board[0] or None in board[1] or None in board[2]:
        print("Available Spaces")
        return False
    else:
        print("Not the end!")
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    print("running player")
    who = winner(board)
    if who == X:
        return 1
    if who == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    currentactions = actions(board)
    if player(board) == X:
        vT = -math.inf
        move = set()
        for action in currentactions:
            v, count = minvalue(result(board, action), 0)
            if v > vT:
                vT = v
                move = action
    else:
        vT = math.inf
        move = set()
        for action in currentactions:
            v, count = maxvalue(result(board, action), 0)
            if v < vT:
                vT = v
                move = action
    print(count)
    return move

def maxvalue(board, count):
    """
    Calculates the max value of a given board recursively together with minvalue
    """

    if terminal(board): return utility(board), count + 1

    v = -math.inf
    posactions = actions(board)

    for action in posactions:
        vret, count = minvalue(result(board, action), count)
        v = max(v, vret)

    return v, count + 1

def minvalue(board, count):
    """
    Calculates the min value of a given board recursively together with maxvalue
    """

    if terminal(board): return utility(board), count + 1

    v = math.inf
    posactions = actions(board)

    for action in posactions:
        vret, count = maxvalue(result(board, action), count)
        v = min(v, vret)

    return v, count + 1
