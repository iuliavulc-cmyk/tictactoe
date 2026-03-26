# Tic-Tac-Toe Constitution

## Core Principles

### I. Clean Code
All code must be readable, well-structured, and maintainable. Functions do one thing. Names are descriptive. Game logic is fully separated from UI rendering. No magic numbers — use named constants. Follow PEP 8 and Python best practices throughout.

### II. Attractive UI
The user interface must be visually polished and intuitive. Use color, spacing, and clear visual hierarchy to make the board easy to read. Provide immediate feedback for every action: valid moves, invalid moves, turn changes, wins, and draws. The winning line must be visually highlighted.

### III. Minimal Dependencies
The project must rely on Python's standard library as much as possible. External packages are permitted only when they provide significant UI value that cannot be reasonably achieved with built-in modules. Every dependency must be explicitly justified. Zero dependencies is the ideal target.

### IV. Strict Game Rules (NON-NEGOTIABLE)
The following rules define the valid structure and state transitions and must be enforced at all times:
- The board consists of exactly 9 positions arranged in a 3×3 grid
- Each position may be empty or contain exactly one mark (X or O) — never more than one
- Two players (X and O) alternate turns, starting with X
- Only the current player may place a mark, and only into an empty position
- Once placed, a mark cannot be modified or overwritten
- The number of marks placed by each player must differ by no more than one at any point
- A player wins by occupying all three positions in a row, column, or diagonal
- When a winning line is formed, the game ends immediately
- If all 9 positions are filled with no winning line, the game ends in a draw
- Once the game has ended (win or draw), no additional moves may be made

### V. Separation of State and Presentation
The game state — consisting of the current board configuration, the identity of the player whose turn it is, and the game outcome status (in progress, win, or draw) — must be modeled explicitly and independently from how it is displayed. State transitions must be validated before being applied.

## Technology Stack

- **Language**: Python 3.10+
- **Dependencies**: Standard library only (unless explicitly justified for UI enhancement)
- **Testing**: unittest or pytest
- **Style**: PEP 8 enforced via linter

## Development Workflow

- Game logic must have unit tests covering all win conditions, draw detection, invalid move rejection, and turn enforcement
- UI changes must be manually verified for visual correctness
- Commits should be small and focused on a single concern
- No game rule may be relaxed or bypassed for convenience

## Governance

This constitution is the authoritative source of truth for the Tic-Tac-Toe project. All code must comply with the principles and game rules defined above. The game rules in Section IV are non-negotiable and override any implementation convenience. Deviations require explicit justification and documentation.

**Version**: 1.0.0 | **Ratified**: 2026-03-26 | **Last Amended**: 2026-03-26
