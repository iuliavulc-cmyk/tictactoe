"""
Minimax AI implementation for Tic-Tac-Toe.
"""

from src.models import Mark

def minimax(board, is_maximizing, depth=0):
    """
    Minimax algorithm for Tic-Tac-Toe.
    Args:
        board (list): Current board state as a list of 9 elements.
        is_maximizing (bool): True if computer's turn, False if player's turn.
        depth (int): Current recursion depth (for scoring).
    Returns:
        tuple: (score, move)
    """
    winner = check_winner(board)
    if winner == Mark.O:
        return 1, None  # Computer wins
    elif winner == Mark.X:
        return -1, None  # Player wins
    elif all(cell != Mark.EMPTY for cell in board):
        return 0, None  # Draw

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if board[i] == Mark.EMPTY:
                board[i] = Mark.O
                score, _ = minimax(board, False, depth+1)
                board[i] = Mark.EMPTY
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for i in range(9):
            if board[i] == Mark.EMPTY:
                board[i] = Mark.X
                score, _ = minimax(board, True, depth+1)
                board[i] = Mark.EMPTY
                if score < best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move

def check_winner(board):
    lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for line in lines:
        if board[line[0]] != Mark.EMPTY and all(board[line[0]] == board[i] for i in line):
            return board[line[0]]
    return None
