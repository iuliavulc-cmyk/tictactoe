from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Optional

class Mark(Enum):
    X = "X"
    O = "O"
    EMPTY = " "

class GameMode(Enum):
    PVP = "Player vs Player"
    PVC = "Player vs Computer"

class GameStatus(Enum):
    IN_PROGRESS = auto()
    X_WINS = auto()
    O_WINS = auto()
    DRAW = auto()

@dataclass
class GameState:
    board: List[Mark] = field(default_factory=lambda: [Mark.EMPTY]*9)
    current_player: Mark = Mark.X
    status: GameStatus = GameStatus.IN_PROGRESS
    mode: GameMode = GameMode.PVP
    winning_line: Optional[List[int]] = None
