import pytest
from src.models import GameState, Mark, GameStatus, GameMode
from src.game_logic import make_move, check_win, check_draw, get_computer_move

def test_make_move_valid():
    state = GameState()
    new_state = make_move(state, 0)
    assert new_state.board[0] == Mark.X
    assert new_state.current_player == Mark.O
    assert new_state.status == GameStatus.IN_PROGRESS

def test_make_move_invalid():
    state = GameState(board=[Mark.X]+[Mark.EMPTY]*8)
    new_state = make_move(state, 0)
    assert new_state is state or new_state.board == state.board

def test_win_detection():
    board = [Mark.X, Mark.X, Mark.X, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY, Mark.EMPTY]
    assert check_win(board, Mark.X) == [0,1,2]
    board = [Mark.O, Mark.EMPTY, Mark.EMPTY, Mark.O, Mark.EMPTY, Mark.EMPTY, Mark.O, Mark.EMPTY, Mark.EMPTY]
    assert check_win(board, Mark.O) == [0,3,6]

def test_draw_detection():
    board = [Mark.X, Mark.O, Mark.X, Mark.X, Mark.O, Mark.O, Mark.O, Mark.X, Mark.X]
    assert check_draw(board)
    board = [Mark.X, Mark.O, Mark.EMPTY, Mark.X, Mark.O, Mark.O, Mark.O, Mark.X, Mark.X]
    assert not check_draw(board)

def test_get_computer_move():
    board = [Mark.X, Mark.O, Mark.X, Mark.X, Mark.O, Mark.O, Mark.O, Mark.X, Mark.EMPTY]
    move = get_computer_move(board)
    assert move == 8
    board = [Mark.X]*9
    move = get_computer_move(board)
    assert move == -1
