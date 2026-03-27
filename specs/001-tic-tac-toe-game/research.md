# Research: Tic Tac Toe Game

## Decisions & Rationale

### Language & GUI
- **Decision**: Python 3.12 with tkinter
- **Rationale**: tkinter is included in the Python standard library, requires no external dependencies, and is sufficient for a simple grid-based game. Python 3.12 is stable and widely available.
- **Alternatives considered**: pygame (requires pip install, more suited for animation-heavy games), PyQt (heavier, not needed for this scope)

### Game State Model
- **Decision**: Central GameState dataclass with board, current player, status, mode, and winning line
- **Rationale**: Clean separation of logic and UI, enables pure-function testing, and easy state resets
- **Alternatives considered**: Mutable global state (harder to test), OOP-heavy design (overkill for this scope)

### Computer Move Logic
- **Decision**: Computer selects a random empty square
- **Rationale**: Per spec clarification, no heuristics or AI difficulty required; random is simple and testable
- **Alternatives considered**: Heuristic/blocking AI, minimax (out of scope)

### UI Navigation
- **Decision**: Mode selection screen before each game, "New Game" returns to mode selection
- **Rationale**: Consistent, user-friendly navigation; matches clarified requirements
- **Alternatives considered**: In-game mode toggle, persistent mode (adds complexity)

### No Score Tracking
- **Decision**: No scoreboard or session win tracking
- **Rationale**: Per spec clarification, each game is independent
- **Alternatives considered**: Session scoreboard (out of scope)
