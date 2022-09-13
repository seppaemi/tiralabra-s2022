from turtle import pos
import pygame
from modules.multiplayer import Play
from UI.menu_UI import Menu_UI

class Menu:

    def __init__(self):
        self.ui = Menu_UI()
        self.clicked = False

    def run_menu(self):
        pygame.init()
        self.ui.setup()
        self.menu_loop()

    def mouse_click(self, position):
        if self.ui.multiplayer_button.collidepoint(position):
            multiplayer_game = Play()
            multiplayer_game.run()
            self.ui.reset_caption()
        if not self.clicked:
            if self.ui.singleplayer_button.collidepoint(position):
                self.clicked = True

    def check_events(self):
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
        if self.clicked:
            self.ui.draw_screen_if_clicked()
        else:
            self.ui.draw_screen_not_clicked()

    def menu_loop(self):
        while True:
            self.check_events()
            self.draw_screen()
    
    def reset_menu(self):
        self.clicked = False