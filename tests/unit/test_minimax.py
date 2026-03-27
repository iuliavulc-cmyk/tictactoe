from src.game_logic import is_valid_move
    def test_is_valid_move(self):
        board = ['X', 'O', None, None, 'X', 'O', None, None, None]
        self.assertTrue(is_valid_move(board, 2))
        self.assertFalse(is_valid_move(board, 0))
        self.assertFalse(is_valid_move(board, 9))
import unittest
from src.ai.minimax import minimax

class TestMinimax(unittest.TestCase):
    def test_minimax_optimal(self):
        # Test that computer (O) never loses if both play optimally
        from src.models import Mark
        from src.ai.minimax import minimax
        # Board: X |   |  
        #         - + - + -
        #           |   |  
        #         - + - + -
        #           |   |  
        board = [Mark.X, Mark.EMPTY, Mark.EMPTY,
                 Mark.EMPTY, Mark.EMPTY, Mark.EMPTY,
                 Mark.EMPTY, Mark.EMPTY, Mark.EMPTY]
        # Computer's turn (O)
        score, move = minimax(board, is_maximizing=True)
        # The best score should be 0 (draw) or 1 (win for O)
        self.assertIn(score, [0, 1])

if __name__ == "__main__":
    unittest.main()
