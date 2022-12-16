"""

"""
import sys
import unittest
import random

sys.path.append('../../src/board')

from board import StandardBoard

class TestStandardBoard(unittest.TestCase):
    def setUp(self):
        self.board = StandardBoard.new_board()

    def test_to_see_if_the_creation_of_a_standard_board_is_successful_or_not(self) -> None:
        self.assertTrue(self.board.get_width() == 8 and self.board.get_height() == 8)

    def test_to_see_if_index_error_is_raised_if_we_try_to_retrieve_a_piece_for_which_the_x_index_is_out_of_bounds(self) -> None:
        x = random.choice([-1, self.board.get_width() + 1])
        y = random.randint(0, self.board.get_height() - 1)
        with self.assertRaises(IndexError):
            self.board.get_piece(x, y)
        
    def test_to_see_if_index_error_is_raised_if_we_try_to_retrieve_a_piece_for_which_the_y_index_is_out_of_bounds(self) -> None:
        x = random.randint(0, self.board.get_width() - 1) 
        y = random.choice([-1, self.board.get_height() + 1])
        with self.assertRaises(IndexError):
            self.board.get_piece(x, y)

if __name__ == '__main__':
    unittest.main()