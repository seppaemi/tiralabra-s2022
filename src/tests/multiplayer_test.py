"""Moduuli, joka sisältää luokan TestMultiplayer"""
import unittest
from modules.multiplayer import Play


class TestMultiplayer(unittest.TestCase):
    """Luokka, joka vastaa multiplayerin testaamisesta"""

    def setUp(self):
        """Asettaa pelin testattavaan tilaan"""
        self.play = Play()

    def test_after_setup_running_is_False(self):
        """Testaa, onko peli käynnissä setupin asetettua"""
        self.assertEqual(False, self.play.running)

    def test_after_setup_game_is_not_over(self):
        """Testaa, onko peli ohi setupin asetuttua"""
        self.assertEqual(False, self.play.game_over)

    def test_after_setup_ai_has_correct_value(self):
        """Testaa tekoälyn arvoa setupin asetuttua multiplayerissä"""
        self.assertEqual(False, self.play.ai)

    def test_after_setup_all_slots_are_empty(self):
        """Testaa, ettei missään kohdassa ole pelimerkkiä,
        ennen aloitusta"""
        all_empty = True
        for y in range(6):
            for x in range(7):
                if self.play.board[y][x] != 0:
                    all_empty = False
        self.assertEqual(True, all_empty)

    def test_red_wins_ends_game(self):
        """Testaa pelin päättymisen punaisen voitettua"""
        self.play.red_wins()
        self.assertEqual(True, self.play.game_over)

    def test_green_wins_ends_game(self):
        """Testaa pelin päättymisen vihreän voitettua"""
        self.play.green_win()
        self.assertEqual(True, self.play.game_over)

    def test_four_hor_green_wins_game(self):
        """testaa vaakatasossa vihreän voittoa"""
        self.play.board[2][1] = 1
        self.play.board[2][2] = 1
        self.play.board[2][3] = 1
        self.play.board[2][4] = 1
        self.play.check_for_win()
        self.assertEqual(True, self.play.green_win)

    def test_four_hor_red_wins_game(self):
        """Testaa vaakatasossa punaisen voittoa"""
        self.play.board[4][2] = 2
        self.play.board[4][3] = 2
        self.play.board[4][4] = 2
        self.play.board[4][5] = 2
        self.play.check_for_win()
        self.assertEqual(True, self.play.red_wins)

    def test_four_hor_green_ends_game(self):
        """Testaa näljän vaakatasossa vihreän voittoa"""
        self.play.board[3][4] = 1
        self.play.board[3][3] = 1
        self.play.board[3][2] = 1
        self.play.board[3][1] = 1
        self.play.check_for_win()
        self.assertEqual(True, self.play.game_over)

    def test_four_vert_green_wins_game(self):
        """Testaa pystyssä vihreän voittoa"""
        self.play.board[2][3] = 1
        self.play.board[3][3] = 1
        self.play.board[4][3] = 1
        self.play.board[5][3] = 1
        self.play.check_for_win()
        self.assertEqual(True, self.play.green_win)

    def test_four_vert_red_wins_game(self):
        """testaa pystyssä punaisen voittoa"""
        self.play.board[5][5] = 2
        self.play.board[3][5] = 2
        self.play.board[4][5] = 2
        self.play.board[2][5] = 2
        self.play.check_for_win()
        self.assertEqual(True, self.play.red_wins)

    def test_four_down_diag_green_wins_game(self):
        """Testaa viistossa alas vihreän voittoa"""
        self.play.board[1][1] = 1
        self.play.board[2][2] = 1
        self.play.board[3][3] = 1
        self.play.board[4][4] = 1
        self.play.check_for_win()
        self.assertEqual(True, self.play.green_win)

    def test_four_down_diag_red_wins_game(self):
        """Testaa viistossa alas punaisen voittoa"""
        self.play.board[2][1] = 2
        self.play.board[3][2] = 2
        self.play.board[4][3] = 2
        self.play.board[5][4] = 2
        self.play.check_for_win()
        self.assertEqual(True, self.play.red_wins)

    def test_four_up_diag_red_wins_game(self):
        """Testaa viistossa ylös punaisen voittoa"""
        self.play.board[4][2] = 2
        self.play.board[3][3] = 2
        self.play.board[2][4] = 2
        self.play.board[1][5] = 2
        self.play.check_for_win()
        self.assertEqual(True, self.play.red_wins)

    def test_four_up_diag_green_wins_game(self):
        """Testaa viistossa ylös vihreän voittoa"""
        self.play.board[2][5] = 1
        self.play.board[3][4] = 1
        self.play.board[4][3] = 1
        self.play.board[5][2] = 1
        self.play.check_for_win()
        self.assertEqual(True, self.play.green_win)

    def test_restart_game_clean_board(self):
        """Testaa uudelleenaloituksen tyhjentävän pelilaudan"""
        self.play.board = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 2, 0, 0, 0],
                           [0, 0, 1, 2, 1, 1, 0],
                           [0, 0, 1, 2, 1, 2, 0],
                           [0, 2, 1, 1, 2, 2, 0]]
        self.play.restart()
        restarted = True
        if self.play.game_over:
            restarted = False
        if self.play.red_wins:
            restarted = False
        if self.play.green_win:
            restarted = False
        if not self.play.running:
            restarted = False
        for y in range(6):
            for x in range(7):
                if self.play.board[y][x] != 0:
                    restarted = False
        self.assertEqual(False, restarted)

    def test_game_ends_in_tie_when_board_full_and_no_win(self):
        """Testaa että tulee tasapeli jos laita on täynnä eikä
        kumpikaan voita"""
        self.play.board = [[2, 2, 1, 2, 1, 1, 2],
                           [1, 1, 2, 1, 2, 2, 1],
                           [2, 2, 2, 1, 1, 1, 2],
                           [1, 1, 2, 1, 1, 2, 1],
                           [2, 2, 1, 2, 2, 2, 1],
                           [1, 2, 2, 1, 1, 2, 1]]
        self.play.check_for_tie()
        self.assertEqual(True, self.play.tie)

    def test_column_full_returns_correct(self):
        """Testaa palautuuko oikea arvo kun rivi täyttyy"""
        self.play.board = [[2, 2, 1, 2, 1, 1, 2],
                           [1, 1, 2, 1, 2, 2, 1],
                           [2, 2, 2, 1, 1, 1, 2],
                           [1, 1, 2, 1, 1, 2, 1],
                           [2, 2, 1, 2, 2, 2, 1],
                           [1, 2, 2, 1, 1, 2, 1]]
        self.assertEqual(True, self.play.full_column(2))

    def test_mouse_click_works_on_green(self):
        """Testaa että vihreää klikatessa toiminnot ovat oikein"""
        self.play.green_turn = True
        self.play.mouse((435, 250))
        self.assertEqual([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0]],
                         self.play.board)

    def test_mouse_click_works_changes_turn_and_works_on_red(self):
        """Testaa että klikatessa vuoro vaihtuu punaiseen ja punaista
        klikatessa toiminnot ovat oikein"""
        self.play.green_turn = True
        self.play.mouse((435, 250))
        self.play.mouse((346, 577))
        self.assertEqual([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 2, 1, 0, 0]],
                         self.play.board)

    def test_game_stops_running_if_clicked_after_game_over(self):
        """Peli ei ole käynnissä kun sen päätyttyä hiirtä klikataan"""
        self.play.game_over = True
        self.play.mouse((250, 456))
        self.assertEqual(False, self.play.running)

    def test_mouse_clicked_does_nothing_if_full_colum_is_clicked(self):
        """Testaa ettei täyttä saraketta klikatessa siihen saa lisättyä
        enää pelimerkkejä"""
        self.play.board = [[0, 0, 2, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 2, 2, 0, 0],
                           [0, 0, 0, 1, 2, 0, 0],
                           [0, 0, 1, 2, 1, 0, 0],
                           [0, 1, 2, 1, 2, 2, 0]]
        self.play.green_turn = True
        self.play.mouse((225, 467))
        self.assertEqual([[0, 0, 2, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 2, 2, 0, 0],
                          [0, 0, 0, 1, 2, 0, 0],
                          [0, 0, 1, 2, 1, 0, 0],
                          [0, 1, 2, 1, 2, 2, 0]], self.play.board)
