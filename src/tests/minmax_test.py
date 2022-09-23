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
        self.board = [[0,0,0,2,0,0,0], 
                      [0,0,0,1,0,0,0],
                      [0,0,0,2,0,0,0],
                      [0,0,0,1,2,0,0],
                      [0,0,1,2,1,1,0],
                      [0,1,2,1,2,2,1]]
        self.assertEqual((2,4), mm_ab.best_move_check(self.board, 5))
    
    def test_low_free_gives_correct_y_axis_value(self):
        """Testaa että löytyy alin vapaa"""
        self.assertEqual(1, mm_ab.low_free(self.board, 3))
