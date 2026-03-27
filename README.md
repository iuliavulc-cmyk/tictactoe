# Tic Tac Toe Game

A simple desktop Tic Tac Toe game with Player vs Player and Player vs Computer modes, built with Python 3.12 and tkinter.

## Features
- 3x3 grid, two modes: PvP and PvC
- Win/draw detection, board lock after game ends
- Mode selection and new game reset
- Simple, accessible UI

## Running the Game

1. Install Python 3.12+
2. (Optional) Install pytest for tests:
	```sh
	pip install pytest pytest-cov
	```
3. Run the game:
	```sh
	python -m src.main
	```

## Running Tests

```sh
pytest tests/
pytest --cov=src --cov-report=term-missing
```

## Project Structure

- `src/` — Source code
- `tests/` — Unit and integration tests
- `specs/001-tic-tac-toe-game/` — Feature specification and planning docs
# tictactoe
