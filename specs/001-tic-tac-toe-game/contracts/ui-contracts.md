# UI Contract: Tic Tac Toe Game

## Mode Selection Screen
- Two buttons: "Player vs Player" and "Player vs Computer"
- Selecting a mode transitions to the game board

## Game Board Screen
- 3×3 grid of clickable squares (buttons)
- Status label: shows current turn, win, or draw
- Winning squares are highlighted when a win occurs
- "New Game" button returns to mode selection
- Board is locked (no input) after win or draw

## General
- All UI text is clear and unambiguous
- No sound or animation required
- No persistent state or score tracking
