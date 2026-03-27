# Implementation Plan: Tic Tac Toe Game

**Branch**: `001-tic-tac-toe-game` | **Date**: 2026-03-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-tic-tac-toe-game/spec.md`

## Summary

The feature will be organized around a central game state that represents the board, the active player, and whether the game has ended. User interactions from the Python graphical interface will be translated into game actions that update this state. After each move, the system will evaluate the board to determine if a win or draw has occurred and will update the state accordingly. The UI will always reflect the current state and will stop accepting moves once the game is finished. A reset action will return the game to its initial state. If AI mode is enabled, the system will generate an automatic move after the human plays, using the same state‑update flow as human moves.

## Technical Context

- **Language/Version**: Python 3.12
- **Primary Dependencies**: tkinter (stdlib)
- **Storage**: N/A (no persistence)
- **Testing**: pytest + pytest-cov
- **Target Platform**: Desktop (Windows/macOS/Linux)
- **Project Type**: Desktop GUI application
- **Performance Goals**: Instant response (<100ms per move), computer move <1s
- **Constraints**: Offline-only, single device, no external deps beyond stdlib
- **Scale/Scope**: 2 screens (mode selection, game board), ~5 source modules

## Constitution Check

No constitution gates enforced (template only). Proceed.

## Project Structure

```
specs/001-tic-tac-toe-game/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── ui-contracts.md
├── checklists/
│   └── requirements.md
└── tasks.md              # Created by /speckit.tasks, not this command

src/
├── __init__.py
├── main.py               # Entry point — launches tkinter app
├── models.py             # GameState, Board, Mark, GameMode, GameStatus enums/dataclasses
├── game_logic.py         # Pure functions: make_move, check_win, check_draw, get_computer_move
├── ui/
│   ├── __init__.py
│   ├── app.py            # Main tkinter App class — manages screen transitions
│   ├── mode_screen.py    # Mode selection screen (PvP / PvC buttons)
│   └── game_screen.py    # Game board screen (3x3 grid, status label, New Game button)

tests/
├── __init__.py
├── test_models.py        # GameState creation, reset, field integrity
├── test_game_logic.py    # Win detection (all 8 lines), draw detection, move validation, computer move
├── test_integration.py   # Full game flows: PvP win, PvP draw, PvC win, PvC draw, new game reset
```

**Structure Decision**: Single-project layout. Game logic is pure Python (no tkinter dependency) in `models.py` + `game_logic.py`. UI layer in `src/ui/` reads and updates GameState. This separation means ~90% of logic is unit-testable without GUI.

## Steps

### Phase 1: Core Game State & Logic (P1 stories — no GUI needed)

1. **Create `src/models.py`** — Define `Mark` enum (X, O, EMPTY), `GameMode` enum (PVP, PVC), `GameStatus` enum (IN_PROGRESS, X_WINS, O_WINS, DRAW), and `GameState` dataclass (board: list[Mark], current_player: Mark, status: GameStatus, mode: GameMode, winning_line: list[int] | None).

2. **Create `src/game_logic.py`** — Implement pure functions:
   - `make_move(state, position) -> GameState` — validates position is empty and game is in progress, places mark, checks for win/draw, switches turn. Returns new state (or unchanged if invalid).
   - `check_win(board, mark) -> list[int] | None` — checks all 8 lines (3 rows, 3 cols, 2 diagonals), returns winning indices or None.
   - `check_draw(board) -> bool` — returns True if no empty squares remain.
   - `get_computer_move(board) -> int` — picks uniformly random from empty squares.
   - `new_game(mode) -> GameState` — returns fresh initial state for given mode.

3. **Create `tests/test_models.py`** — Test GameState creation, field defaults, enum values.

4. **Create `tests/test_game_logic.py`** — Test:
   - `make_move`: valid move updates board+turn, invalid move (occupied square) returns unchanged state, move on finished game returns unchanged state
   - `check_win`: all 8 winning lines for X and O, no false positives on non-winning boards
   - `check_draw`: full board with no winner → True, board with empty squares → False
   - `get_computer_move`: returns index of an empty square, handles single-remaining-square case
   - `new_game`: returns empty board, X's turn, IN_PROGRESS status
   - Edge case: winning move that also fills board → status is win (not draw)

*Steps 1-2 are parallel. Steps 3-4 depend on 1-2.*

### Phase 2: GUI — Mode Selection & Game Board (P2 stories)

5. **Create `src/ui/app.py`** — Main `TicTacToeApp(tk.Tk)` class that manages two frames: mode selection and game board. Provides `show_mode_screen()` and `show_game_screen(mode)` methods to switch between them. *Depends on step 1.*

6. **Create `src/ui/mode_screen.py`** — `ModeScreen(tk.Frame)` with two buttons: "Player vs Player" and "Player vs Computer". Each button calls `app.show_game_screen(GameMode.PVP)` or `app.show_game_screen(GameMode.PVC)`. *Parallel with step 7.*

7. **Create `src/ui/game_screen.py`** — `GameScreen(tk.Frame)` containing:
   - 3×3 grid of `tk.Button` widgets for the board
   - Status label showing "Player X's turn" / "Player O wins!" / "It's a draw!"
   - "New Game" button that calls `app.show_mode_screen()`
   - Click handler: calls `game_logic.make_move()`, updates button text/colors, checks status
   - Win highlighting: changes background color of winning squares (e.g., green)
   - Board lock: disables all buttons when `status != IN_PROGRESS`
   - PvC auto-move: after human move, if game still in progress and mode is PVC, calls `get_computer_move()` via `root.after(300, ...)` for slight delay
   *Depends on steps 1-2, 5.*

8. **Create `src/main.py`** — Entry point: instantiates `TicTacToeApp`, calls `mainloop()`. *Depends on step 5.*

### Phase 3: Integration Tests & Polish

9. **Create `tests/test_integration.py`** — Full game flow tests using game_logic functions only (no GUI):
   - Play a full PvP game resulting in X win → verify status, winning_line
   - Play a full PvP game resulting in draw → verify status
   - Play PvC game: human move followed by computer auto-move → verify alternation
   - New game resets completely
   - Rapid-move edge case: calling make_move on ended game is a no-op
   *Depends on Phase 1.*

10. **Manual GUI verification** — Run the app and walk through each acceptance scenario from the spec visually. *Depends on Phase 2.*

## Relevant Files

- `src/models.py` — Define `Mark`, `GameMode`, `GameStatus` enums and `GameState` dataclass; central data model for the entire app
- `src/game_logic.py` — All pure game logic: `make_move()`, `check_win()`, `check_draw()`, `get_computer_move()`, `new_game()`
- `src/ui/app.py` — Screen manager: `show_mode_screen()`, `show_game_screen(mode)`
- `src/ui/mode_screen.py` — Mode selection: two buttons → triggers screen transition
- `src/ui/game_screen.py` — Board rendering, click handling, win highlighting, PvC auto-move via `root.after()`
- `src/main.py` — Entry point
- `tests/test_game_logic.py` — Core logic tests: all 8 win lines, draw, move validation, computer move randomness
- `tests/test_integration.py` — Full game flows without GUI

## Verification

1. `pytest tests/test_models.py tests/test_game_logic.py -v` — All unit tests pass (win detection for all 8 lines, draw detection, move validation, computer random move)
2. `pytest tests/test_integration.py -v` — All integration flow tests pass (PvP win, PvP draw, PvC flow, new game reset)
3. `pytest --cov=src --cov-report=term-missing` — Coverage ≥90% on `models.py` and `game_logic.py`
4. Manual: Run `python -m src.main`, select PvP mode, play to X win → verify highlight + message + board lock
5. Manual: Play to draw → verify draw message + board lock
6. Manual: Click "New Game" → verify return to mode selection
7. Manual: Select PvC mode, make one move → verify computer responds automatically
8. Manual: Click occupied square → verify nothing happens

## Decisions

- **tkinter over pygame/PyQt**: stdlib, zero install, sufficient for a grid of buttons + labels
- **Pure logic separation**: `game_logic.py` has no tkinter imports — makes it fully unit-testable
- **Immutable-ish state**: `make_move()` returns a new `GameState` rather than mutating — easier to reason about and test
- **`root.after()` for computer move delay**: 300ms delay gives visual feedback that the computer is "thinking" and prevents the UI from appearing to skip
- **No `random.seed` in prod**: Tests that verify computer randomness will mock `random.choice`
- **Scope boundary**: No animations, no sound, no score tracking, no AI heuristics — per spec clarifications
