# Data Model: Tic Tac Toe Game

## Entities

### GameState (dataclass)
- board: list[Mark] (length 9, row-major order)
- current_player: Mark (X or O)
- status: GameStatus (IN_PROGRESS, X_WINS, O_WINS, DRAW)
- mode: GameMode (PVP, PVC)
- winning_line: list[int] | None (indices of winning squares, or None)

### Mark (enum)
- X
- O
- EMPTY

### GameMode (enum)
- PVP
- PVC

### GameStatus (enum)
- IN_PROGRESS
- X_WINS
- O_WINS
- DRAW

### Move (function)
- make_move(state: GameState, position: int) -> GameState
- get_computer_move(board: list[Mark]) -> int

## Relationships
- GameState.board is updated by make_move()
- GameState.status is updated by check_win() and check_draw()
- GameState.mode determines if computer moves are triggered
- winning_line is set when a win is detected
