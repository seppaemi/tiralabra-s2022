
"""Moduuli, joka sisältää luokan SinglePlayer"""
from modules.multiplayer import Play
from modules import mm_ab

class SinglePlayer(Play):
    """Perii luokan Play ja vastaa tekoälyä vastaan pelaamisesta.
    Attributes:
        Perii Play luokan attribuutit
        header: otsikko pelille merkkojonona
        level: Keroo minmaxissa käytettävän syvyyden lukuna
        mm_ab: Kertoo pelataanko tekoälyä vastaan, tässä tilanteessa true"""

    def __init__(self, level):
        """Konstruktori, jossa level kuvaa syvyyttä millä tekoäly pelaa"""
        super().__init__()
        self.title = "tekoälyä vastaan"
        self.level = level
        self.ai = True
    
    def ai_turn(self):
        """Vastaa tekoälyn pelivuorosta"""
        y, x = mm_ab.best_move_check(self.board, self.level)
        self.board[y][x] = 2
        self.green_turn = True

    def mouse(self, pos):
        """Tekee siirron hiiren klikkauksen mukaan"""
        if not self.game_over:
            (x,y) = pos
            y -= 100
            y = y//100
            x = x//100

            if not self.full_column(x):
                for i in range(5,-1,-1):
                    if self.board[i][x] == 0:
                        if self.green_turn:
                            self.board[i][x] = 1
                            self.green_turn = False
                            self.ui.draw_screen(self.board, self.game_over,
                                                self.end_tie, self.green_win,
                                                self.red_win, self.ai,
                                                self.green_turn, self.mouse_pos)
                            self.ai_turn()
                            break
                        else:
                            break

            self.check_for_win()
            self.check_for_tie()

        else:
            self.running = False
