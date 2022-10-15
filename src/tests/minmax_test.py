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
  
    def test_ai_making_line_and_blocking_one(self):
        """Testaa tekeekö tekoäly optimoidumman siirron, kun voi
        samalla estää ja tehdä rivin"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,2,1,2],
                      [0,0,2,2,1,1,1],
                      [0,0,2,1,1,2,1]]
        self.assertEqual((2,5), mm_ab.best_move_check(self.board, 4))
  
    def test_smart_move_if_win_in_two(self):
        """Testataan tekeekö tekoäly voiton kahden päästä"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0],
                      [0,0,0,2,1,0,0],
                      [0,2,0,2,1,2,0],
                      [1,1,2,1,2,1,1]]
        self.assertEqual((4,2), mm_ab.best_move_check(self.board, 4))

    def test_move_after_smart_move(self):
        """testataan minkä siirron tekoäly tekee 
        äskeisen siirron jälkeen"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0],
                      [0,0,1,2,1,0,0],
                      [0,2,2,2,1,2,0],
                      [1,1,2,1,2,1,1]]
        self.assertEqual((4,0), mm_ab.best_move_check(self.board, 2))

    def test_smart_move_if_lose_in_two(self):
        """Testaa ai siirtoa jos toisella voitto kahden siirron
        päästä"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,2,0,1,0,1],
                      [0,2,1,1,1,2,1],
                      [1,1,2,2,2,1,2]]
        self.assertEqual((3,3), mm_ab.best_move_check(self.board, 4))

    def test_to_win_when_can_block(self):
        """Testaa tilannetta missä molemmilla mahdollisuus voittoon"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,2,1,0,0],
                      [0,0,2,2,2,1,0],
                      [0,1,1,1,2,1,1]]
        self.assertEqual((4,1), mm_ab.best_move_check(self.board, 4))

    def test_block_if_no_chance_to_win(self):
        """testaa tilannetta jossa tekoäly ei voi voittaa
        mutta voi päättyä voittoon tai tasapeliin"""
        self.board = [[0,0,0,1,2,1,1], 
                      [1,2,1,1,1,2,1],
                      [2,2,1,1,1,2,2],
                      [2,1,2,2,1,1,1],
                      [1,1,2,1,2,2,2],
                      [1,2,2,1,1,1,2]]
        self.assertEqual((0,2), mm_ab.best_move_check(self.board, 4))

    def the_empty_board_fot_tests(self):
        """tyhjä jota käytän testeihin MUISTA POISTAA"""
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
