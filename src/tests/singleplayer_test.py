import unittest
from modules.singleplayer import SinglePlayer
EASY = 2
MEDIUM = 4 
HARD = 6
class TestSinglePlayer(unittest.TestCase):
    """Testataan singleplayeriä"""
    def setUp(self):
        self.play = SinglePlayer(EASY)

    def test_title_when_setup(self):
        """Testaa että setup asettaa oikean otsikon"""
        self.assertEqual("tekoälyä vastaan", self.play.title)

    def test_if_ai_true_after_setup(self):
        """Testataan että tekoäly menee päälle"""
        self.assertEqual(True, self.play.ai)

    def test_level_correctly_setup(self):
        """Testataan oikeaa tasoa"""
        self.assertEqual(EASY, self.play.level)

    def test_ai_wins_its_turn(self):
        """Testataan tekoälyn voittoa"""
        self.play.board = [[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,2,0,0],
                            [0,0,0,1,2,1,0],
                            [0,0,0,1,2,1,0]]
        self.play.ai_turn()
        self.assertEqual([[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,2,0,0],
                            [0,0,0,0,2,0,0],
                            [0,0,0,1,2,1,0],
                            [0,0,0,1,2,1,0]], self.play.board)