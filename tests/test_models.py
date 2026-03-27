import pytest
from src.models import GameState, Mark, GameStatus, GameMode

def test_gamestate_defaults():
    state = GameState()
    assert state.board == [Mark.EMPTY]*9
    assert state.current_player == Mark.X
    assert state.status == GameStatus.IN_PROGRESS
    assert state.mode == GameMode.PVP
    assert state.winning_line is None

def test_enum_values():
    assert Mark.X.value == "X"
    assert Mark.O.value == "O"
    assert Mark.EMPTY.value == " "
    assert GameMode.PVP.value == "Player vs Player"
    assert GameMode.PVC.value == "Player vs Computer"
