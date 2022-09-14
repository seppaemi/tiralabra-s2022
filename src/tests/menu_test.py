"""Moduuli joka sisältää luokan TestMenu"""
import unittest
from menu.frontpage import Menu


class TestMenu(unittest.TestCase):
    """Luokka, joka vastaa menun testaamisesta"""
    def setUp(self):
        """Valmistelee testauksen"""
        self.menu = Menu()

    def test_clicked_is_correct_after_setup(self):
        """Testaa, toimiiko menun klikkaaminen"""
        self.assertEqual(False, self.menu.clicked)

    def test_mouse_click_to_singleplayer_game_button_makes_clicked_true(self):
        """Testaa, tuleeko singleplayerin painamisesta vaihtoehdot"""
        self.menu.mouse_click((300, 300))
        self.assertEqual(True, self.menu.clicked)

    def test_reset_menu_makes_clickes_false(self):
        """Testaa, palautuuko menu"""
        self.menu.clicked = True
        self.menu.reset_menu()
        self.assertEqual(False, self.menu.clicked)
