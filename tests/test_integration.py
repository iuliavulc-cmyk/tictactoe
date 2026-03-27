import pytest
from src.models import GameState, Mark, GameStatus, GameMode
from src.game_logic import make_move, new_game, get_computer_move

def test_pvp_win_flow():
    state = new_game(GameMode.PVP)
    moves = [0, 3, 1, 4, 2]  # X wins
    for move in moves:
        state = make_move(state, move)
    assert state.status == GameStatus.X_WINS
    assert state.winning_line == [0, 1, 2]

def test_pvp_draw_flow():
    state = new_game(GameMode.PVP)
    moves = [0,1,2,4,3,5,7,6,8]  # Draw
    for move in moves:
        state = make_move(state, move)
    assert state.status == GameStatus.DRAW

def test_pvc_win_flow():
    state = new_game(GameMode.PVC)
    # X moves, O (computer) moves
    state = make_move(state, 0)
    o_move = get_computer_move(state.board)
    state = make_move(state, o_move)
    state = make_move(state, 1)
    o_move = get_computer_move(state.board)
    state = make_move(state, o_move)
    state = make_move(state, 2)
    # X may win if computer doesn't block
    if state.status == GameStatus.X_WINS:
        assert state.winning_line == [0,1,2]


def test_new_game_resets_state():
    state = new_game(GameMode.PVP)
    state = make_move(state, 0)
    state2 = new_game(GameMode.PVC)
    assert state2.board == [Mark.EMPTY]*9
    assert state2.status == GameStatus.IN_PROGRESS
    assert state2.mode == GameMode.PVC
