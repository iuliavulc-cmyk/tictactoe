
from typing import List, Optional
from src.models import Mark, GameState, GameStatus
import random

def make_move(state: GameState, position: int) -> GameState:
    if state.status != GameStatus.IN_PROGRESS or state.board[position] != Mark.EMPTY:
        return state
    new_board = state.board.copy()
    new_board[position] = state.current_player
    winning_line = check_win(new_board, state.current_player)
    if winning_line:
        return GameState(
            board=new_board,
            current_player=state.current_player,
            status=GameStatus.X_WINS if state.current_player == Mark.X else GameStatus.O_WINS,
            mode=state.mode,
            winning_line=winning_line
        )
    if check_draw(new_board):
        return GameState(
            board=new_board,
            current_player=state.current_player,
            status=GameStatus.DRAW,
            mode=state.mode,
            winning_line=None
        )
    next_player = Mark.O if state.current_player == Mark.X else Mark.X
    return GameState(
        board=new_board,
        current_player=next_player,
        status=GameStatus.IN_PROGRESS,
        mode=state.mode,
        winning_line=None
    )

def check_win(board: List[Mark], mark: Mark) -> Optional[List[int]]:
    lines = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diags
    ]
    for line in lines:
        if all(board[i] == mark for i in line):
            return line
    return None

def check_draw(board: List[Mark]) -> bool:
    return all(cell != Mark.EMPTY for cell in board)

def get_computer_move(board: List[Mark]) -> int:
    empty = [i for i, cell in enumerate(board) if cell == Mark.EMPTY]
    return random.choice(empty) if empty else -1

def new_game(mode) -> GameState:
    from src.models import GameMode
    return GameState(
        board=[Mark.EMPTY]*9,
        current_player=Mark.X,
        status=GameStatus.IN_PROGRESS,
        mode=mode,
        winning_line=None
    )
