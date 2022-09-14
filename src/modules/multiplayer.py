"""Moduuli joka sisältää luokan Play"""
import pygame
from modules import gameplay
from UI.game_UI import Game_UI


class Play:
    """Luokka, joka vastaa kaksinpelin toiminnasta.
    Vihreä aloittaa ja punainnen pelaa sitten.
    Attributes:
    ui: sisältää pelin käyttöliittymästä vastaavan luokan
    board: pelilautaa kuvaava matriisi, 0 = tyhjä, 1 = vihreä,
    2 = punainen
    running: kertoo boolean arvona onko peli käynnissä
    red_win: boolean arvo siitä, onko punainen voittanut pelin
    green_win: boolean arvo siitä, onko vihreä voittanut pelin
    end_tie: boolean arvo siitä, onko peli päättynyt tasapeliin
    game_over: boolean arvo pelin päättymisestä
    green_turn: boolean arvo vihreän pelaajan vuorosta
    ai: boolean arvo siitä, onko peli tekoälyä vastaan. Multiplayer-pelimuodossa
    tämä on false ja yksinpelissä true
    mause_pos: Tuple, joka kertoo hiiren sijiannit koordinaattien pikseleinä
    title: pelin otsikko merkkijonona"""

    def __init__(self):
        """Luokan konstruktori"""
        self.ui = Game_UI()
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False
        self.red_win = False
        self.green_win = False
        self.end_tie = False
        self.game_over = False
        self.green_turn = True
        self.ai = False
        self.mouse_pos = (0, 0)
        self.title = "Kaveria vastaan"

    def run(self):
        """Funktio pelin käynnistykseen"""
        while True:
            pygame.init()
            self.ui.game_UI_setup(self.title)
            self.running = True
            self.gameloop()
            break

    def restart(self):
        """Funktio pelin uudelleenaloitukseen"""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = True
        self.red_win = False
        self.green_win = False
        self.end_tie = False
        self.game_over = False
        self.green_turn = True

    def full_column(self, x):
        """Funktio, joka kertoo onko x:n mukainen sarake täysi
        ja palauttaa sen boolean arvona"""
        return gameplay.check_column_full(self.board, x)

    def green_win(self):
        """Funktio vihreän voitosta"""
        self.green_win = True
        self.game_over = True

    def red_wins(self):
        """Funktio punaisen voitosta"""
        self.red_win = True
        self.game_over = True

    def check_for_win(self):
        """Funktio joka tarkistaa voiton ja kutsuu sen
        avulla voittofunktiota"""
        result = gameplay.check_win(self.board)
        if result == 1:
            self.green_win()
        if result == 2:
            self.red_wins()

    def check_for_tie(self):
        """Funktio joka kertoo tasapelistä ja kutsuu tie() jos on"""
        if gameplay.check_tie(self.board):
            self.tie()

    def tie(self):
        """Funktio tasapelitilanteelle"""
        self.game_over = True
        self.end_tie = True

    def mouse(self, pos):
        """Funktio joka käsitteleen hiiren klikkauksen toiminnot"""
        if not self.game_over:
            (x, y) = pos
            y -= 100
            y = y//100
            x = x//100
            if not self.full_column(x):
                for i in range(5, -1, -1):
                    if self.board[i][x] == 0:
                        if self.green_turn:
                            self.board[i][x] = 1
                            self.green_turn = False
                            break
                        else:
                            self.board[i][x] = 2
                            self.green_turn = True
                            break
            self.check_for_win()
            self.check_for_tie()
        else:
            self.running = False

    def event_check(self):
        """Funktio tapahtumien tarkastamiseen"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.restart()
                if event.key == pygame.K_t:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    self.mouse(pos)
            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = pygame.mouse.get_pos()

    def gameloop(self):
        """Silmukka näytön piirtämiseen tapahtumien avulla"""
        while self.running:
            self.event_check()
            self.ui.draw_screen(self.board, self.game_over,
                                self.end_tie, self.green_win,
                                self.red_win, self.ai,
                                self.green_turn, self.mouse_pos)
