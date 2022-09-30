"""Vastaa testauksesta"""
import unittest
from modules import mm_ab
class TestMinMax(unittest.TestCase):
    """Testataan minmax algortimia ja alpha beta karsintaa"""
    def setUp(self):
        """Luo setupin pelilaudasta"""
        self.board = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,2,0,0,0],
                      [0,0,1,2,1,1,0],
                      [0,0,1,2,1,2,0],
                      [0,2,1,1,2,2,0]]

    def test_best_move_check_works(self):
        """Testaa parhaan siirron arviointia"""
        self.board = ([[0,0,0,2,0,0,0],
                      [0,0,0,1,0,0,0],
                      [0,0,0,2,0,0,0],
                      [0,0,0,1,2,0,0],
                      [0,0,1,2,1,1,0],
                      [0,1,2,1,2,2,1]])
        self.assertEqual((2,4), mm_ab.best_move_check(self.board, 5))

    def test_low_free_gives_correct_y_axis_value(self):
        """Testaa että löytyy alin vapaa"""
        self.assertEqual(1, mm_ab.low_free(self.board, 3))

    def test_count_four_return_correct_when_green_won(self):
        """Testaa palautusta kun vihreä voittaa"""
        self.assertEqual(-1000, mm_ab.count_four([1,1,1,1]))

    def test_count_three_returns_correct_when_green_won(self):
        """Testaa palautusta kun vihreä voittaa"""
        self.assertEqual(-100, mm_ab.count_three([0,1,1,1]))

    def test_count_four_return_correct_when_red_won(self):
        """Testaa palautusta kun punainen voittaa"""
        self.assertEqual(10000, mm_ab.count_four([2,2,2,2]))

    def test_count_three_return_correct_when_red_won(self):
        """Testaa palautusta kun punainen voittaa"""
        self.assertEqual(10, mm_ab.count_three([2,2,2,0]))

    def test_count_four_returns_zero_when_wrong_input(self):
        """Testaa palautusta väärällä syötteellä"""
        self.assertEqual(0, mm_ab.count_four([1,1,1,1,0]))

    def test_count_three_returns_zero_when_wrong_input(self):
        """Testaa palautusta väärällä syötteellä"""
        self.assertEqual(0, mm_ab.count_three([1,1,1,0,0]))

    def test_best_move_ckeck_wins(self):
        """Testaa best move checkin voittoa"""
        self.board[2][4] = 1
        self.assertEqual((1,3), mm_ab.best_move_check(self.board,2))

    def test_best_move_check_blocks(self):
        """Testaa best move checkin taitoa torjua siirto"""
        self.board[1][3] = 1
        self.assertEqual((2,2), mm_ab.best_move_check(self.board,2))

    def test_board_calc_returns_10000_if_three_red_in_row(self):
        """Testaa laudan laskentaa"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0],
                      [1,1,2,2,2,2,1]]
        self.assertEqual(10000, mm_ab.board_calc(self.board))

    def test_board_calc_returns_correct_if_three_green_in_row(self):
        """Testaa laudan laskentaa"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,1,2,0,0],
                      [0,0,1,2,1,0,0],
                      [0,1,2,1,2,2,0]]
        self.assertEqual(-1000, mm_ab.board_calc(self.board))
