"""
Board state representation for Tic-Tac-Toe.
"""

class Board:
    def __init__(self):
        self.state = [[None for _ in range(3)] for _ in range(3)]

    def is_full(self):
        return all(cell is not None for row in self.state for cell in row)

    def make_move(self, row, col, player):
        if self.state[row][col] is None:
            self.state[row][col] = player
            return True
        return False

    def reset(self):
        self.state = [[None for _ in range(3)] for _ in range(3)]
