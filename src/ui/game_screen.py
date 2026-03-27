import tkinter as tk
from src.models import Mark, GameStatus, GameMode
from src.game_logic import make_move, get_computer_move

class GameScreen(tk.Frame):
    def __init__(self, master, state, new_game_callback):
        super().__init__(master)
        self.state = state
        self.new_game_callback = new_game_callback
        self.buttons = []
        self.status_label = None
        self.create_widgets()
        self.update_ui()

    def create_widgets(self):
        grid = tk.Frame(self)
        grid.pack(pady=10)
        for i in range(9):
            btn = tk.Button(grid, text="", width=6, height=3, font=("Arial", 20), command=lambda idx=i: self.on_square_click(idx))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
        self.status_label = tk.Label(self, text="", font=("Arial", 14))
        self.status_label.pack(pady=5)
        new_game_btn = tk.Button(self, text="New Game", command=self.new_game_callback)
        new_game_btn.pack(pady=5)

    def on_square_click(self, idx):
        if self.state.status != GameStatus.IN_PROGRESS or self.state.board[idx] != Mark.EMPTY:
            return
        self.state = make_move(self.state, idx)
        self.update_ui()
        if self.state.mode == GameMode.PVC and self.state.status == GameStatus.IN_PROGRESS and self.state.current_player == Mark.O:
            self.after(300, self.computer_move)

    def computer_move(self):
        idx = get_computer_move(self.state.board)
        if idx != -1:
            self.state = make_move(self.state, idx)
            self.update_ui()

    def update_ui(self):
        for i, btn in enumerate(self.buttons):
            btn.config(text=self.state.board[i].value)
            btn.config(state="normal" if self.state.board[i] == Mark.EMPTY and self.state.status == GameStatus.IN_PROGRESS else "disabled")
            if self.state.winning_line and i in self.state.winning_line:
                btn.config(bg="yellow")
            else:
                btn.config(bg="SystemButtonFace")
        if self.state.status == GameStatus.IN_PROGRESS:
            self.status_label.config(text=f"Turn: {self.state.current_player.value}")
        elif self.state.status == GameStatus.X_WINS:
            self.status_label.config(text="X wins!")
        elif self.state.status == GameStatus.O_WINS:
            self.status_label.config(text="O wins!")
        elif self.state.status == GameStatus.DRAW:
            self.status_label.config(text="Draw!")
