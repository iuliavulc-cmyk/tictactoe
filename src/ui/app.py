import tkinter as tk
from src.ui.mode_screen import ModeScreen
from src.ui.game_screen import GameScreen
from src.models import GameState, GameMode

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.state = None
        self.current_screen = None
        self.show_mode_screen()

    def show_mode_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = ModeScreen(self.root, self.start_game)
        self.current_screen.pack()

    def start_game(self, mode):
        from src.game_logic import new_game
        self.state = new_game(mode)
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = GameScreen(self.root, self.state, self.on_new_game)
        self.current_screen.pack()

    def on_new_game(self):
        self.show_mode_screen()

    def run(self):
        self.root.mainloop()
