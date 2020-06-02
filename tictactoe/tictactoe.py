"""
Tic Tac Toe Player
"""

import math
import random
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
    if board is initial_state():
        return X

    if sum([item.count(X) for item in board]) <= sum([item.count(O) for item in board]):
        return X
    else:
        return O

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list_actions = set()
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item is EMPTY:
                list_actions.add((i, j))
    return list_actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    i, j = action
    # new_board = board[:]
    new_board = copy.deepcopy(board)
    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid move")

    new_board[i][j] = player(board)
    return new_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check for winner in diagonal1
    if board[0][2] != None and board[0][2] == board[2][0] == board[1][1]:
        return board[0][2]
    # Check for winner in diagonal2
    if board[0][0] != None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # Check for winner 3 in a column
    for col in range(len(board)):
        if board[0][col] != None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check for winner 3 in a row
    for row in board:
        if row[0] != None and row[0] == row[1] == row[2]:
            return row[0]

    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or actions(board) == set():  # there is a winner or there is no more empty spaces
        return True

    # if there is no space empty and no winner (the game is over and it is a tie)
    return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) is not None:
        return 1 if winner(board) == X else -1
    else:  # tie
        return 0
# raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) is O:
        best_score, best_action = minimum(board, -math.inf, math.inf)
        print(f"Best score for player O {best_score}" )
        return best_action
    elif player(board) is X:
        best_score, best_action = maximum(board, -math.inf, math.inf)
        print(f"Best score for player X {best_score} ")
        return best_action


def maximum(board, min_val, max_val):

    if terminal(board):
        return (utility(board), None)

    best_score = -math.inf
    best_action = None

    action_list = list(actions(board))
    random.shuffle(action_list)

    for action in action_list:
        best_value, _ = minimum(result(board, action), min_val, max_val)
        if best_value > best_score:
            best_score = best_value
            best_action = action

        if best_score >= max_val:
            break
        min_val = max(min_val, best_score)
    return (best_score, best_action)


def minimum(board, min_val, max_val):

    if terminal(board):
        return (utility(board), None)

    best_action = None
    best_score = math.inf

    action_list = list(actions(board))
    random.shuffle(action_list)

    for action in action_list:
        best_value, _ = maximum(result(board, action), min_val, max_val)
        if best_value < best_score:
            best_score = best_value
            best_action = action

        if best_score <= min_val:
            break
        max_val = min(max_val, best_score)
    return (best_score, best_action)
