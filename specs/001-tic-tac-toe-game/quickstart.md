# Quickstart: Tic Tac Toe Game

## Prerequisites
- Python 3.12+
- tkinter (included with standard Python on most systems)
- pytest (for running tests):
  ```sh
  pip install pytest pytest-cov
  ```

## Running the Game

1. Clone the repository and navigate to the project root.
2. Run the game:
   ```sh
   python -m src.main
   ```
3. Select a mode (Player vs Player or Player vs Computer) and play!

## Running Tests

1. From the project root, run:
   ```sh
   pytest tests/
   ```
2. For coverage:
   ```sh
   pytest --cov=src --cov-report=term-missing
   ```

## Project Structure

- `src/` — Source code
- `tests/` — Unit and integration tests
- `specs/001-tic-tac-toe-game/` — Feature specification and planning docs
