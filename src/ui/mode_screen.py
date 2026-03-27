import tkinter as tk
from src.models import GameMode

class ModeScreen(tk.Frame):
    def __init__(self, master, start_game_callback):
        super().__init__(master)
        self.start_game_callback = start_game_callback
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Select Game Mode", font=("Arial", 16))
        label.pack(pady=10)
        btn_pvp = tk.Button(self, text="Player vs Player", width=20, command=lambda: self.start_game_callback(GameMode.PVP))
        btn_pvp.pack(pady=5)
        btn_pvc = tk.Button(self, text="Player vs Computer", width=20, command=lambda: self.start_game_callback(GameMode.PVC))
        btn_pvc.pack(pady=5)
