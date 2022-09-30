"""Moduuli johon kuuluu luokka Menu
"""
from turtle import pos
import pygame
from modules.multiplayer import Play
from modules.singleplayer import SinglePlayer
from UI.menu_UI import Menu_UI
EASY = 2
MEDIUM = 4
HARD = 6

class Menu:
    """Vastaa valikosta
    Attributes:
            ui: Luokka-olio; vastaa menun käyttöliittymästä
            clicked: boolean arvo, joka kertoo mikäli
            tietokonetta vastaan olevat vaikeustasot on painettu esiin
            """

    def __init__(self):
        self.ui = Menu_UI()
        self.clicked = False

    def run_menu(self):
        """Avaa pelivalikon
        """
        pygame.init()
        self.ui.setup()
        self.menu_loop()

    def mouse_click(self, position):
        """Käsittelee hiiren klikkauksen tapahtumia"""
        if self.ui.multiplayer_button.collidepoint(position):
            multiplayer_game = Play()
            multiplayer_game.run()
            self.ui.reset_caption()
        if not self.clicked:
            if self.ui.singleplayer_button.collidepoint(position):
                self.clicked = True
        else:
            if self.ui.easy_button.collidepoint(position):
                singleplayer_game_easy = SinglePlayer(EASY)
                singleplayer_game_easy.run()
                self.ui.reset_caption()
            if self.ui.medium_button.collidepoint(position):
                singleplayer_game_medium = SinglePlayer(MEDIUM)
                singleplayer_game_medium.run()
                self.ui.reset_caption()
            if self.ui.hard_button.collidepoint(position):
                singleplayer_game_hard = SinglePlayer(HARD)
                singleplayer_game_hard.run()
                self.ui.reset_caption()

    def check_events(self):
        """Tarkastaa tilanteen tapahtumat ja toiminnan"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.mouse_click(position)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    self.reset_menu()

    def draw_screen(self):
        """Piirtää näyön riippuen siitä onko
        vaikeustaso klikattu vai ei"""
        if self.clicked:
            self.ui.draw_screen_if_clicked()
        else:
            self.ui.draw_screen_not_clicked()

    def menu_loop(self):
        """Hyödyntää check eventsiä tarkastaakseen
        tapahtumat silmukkaa hyödyntäen ja piirtää
        näyttöä sammumiseen asti"""
        while True:
            self.check_events()
            self.draw_screen()

    def reset_menu(self):
        self.clicked = False
