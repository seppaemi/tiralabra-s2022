"""Moduuli joka sisältää luokan Menu_UI"""
import pygame

class Menu_UI:
    """Luokka joka huolehtii päävalikon käyttöliittymästä
    Attributes:
    scree_height: näytön korkeus pikseleinä
    screen_width: näytön leveys pikseleinä
    screen: täähn muuttujaan on tallennettuna pelin ikkuna
    singleplayer_button: Kuvaa painiketta jolla valitaan
    vastustajaksi tietokone
    multiplayer_button: Kuvaa painiketta jolla valitaan
    vastustajaksi kaveri
    easy_button: Kuvaa painiketta jolla valitaan vaikeudeksi
    helppo, kun pelataan tietokonetta vastaan
    medium_button: Kuvaa painiketta, jolla valitaan vaikeudeksi
    keskitaso, kun pelataan tietokonetta vastaan
    hard_button: kuvaa painiketta, jolla valitaan vaikeudeksi
    vaikea, kun pelataan tietokonetta vastaan
    bg_color: kuvaa taustaväriä värikoodina
    button_color: kuvaa nappien väriä värikoodina"""
    def __init__(self):
        """Luokan konstruktori"""
        self.screen_height = 700
        self.screen_width = 700
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.singleplayer_button = pygame.Rect(100, 225, 500, 150)
        self.multiplayer_button = pygame.Rect(100, 450, 500, 150)
        self.easy_button = pygame.Rect(50, 240, 150, 120)
        self.medium_button = pygame.Rect(275, 240, 150, 120)
        self.hard_button = pygame.Rect(500, 240, 150, 120)
        self.bg_color = (255, 0, 255)
        self.button_color = (255, 255, 0)

    def setup(self):
        """Funktio, joka tekee käyttöliittymän alkutoimet"""
        pygame.display.set_caption("CONNECT FOUR")
        self.font = pygame.font.SysFont("comicsansms", 45, 1)
        self.font2 = pygame.font.SysFont("comicsansms", 25, 1)

    def reset_caption(self):
        """Funktio joka asettaa otsikon uudelleen"""
        pygame.display.set_caption("CONNECT FOUR")

    def draw_text(self, text, x_value, y_value, font):
        """Funktio joka kirjoittaa näytön tekstit"""
        if font == 1:
            text_area = self.font.render(text, True, (255, 255, 255))
        if font == 2:
            text_area = self.font2.render(text, True, (255, 255, 255))
        self.screen.blit(text_area, (x_value, y_value))

    def draw_button(self, button):
        """Funktio joka piirtää painikkeet"""
        pygame.draw.rect(self.screen, self.button_color, button)

    def draw_screen_if_clicked(self):
        """Funktio piirtämään näyttö kun on valittu pelattavan
        tietokonetta vastaan"""
        self.screen.fill(self.bg_color)
        self.draw_text("VALITSE VASTUSTAJA:", 100, 100, 1)
        self.draw_button(self.multiplayer_button)
        self.draw_text("KAVERI", 240, 500, 1)
        self.draw_levels()
        pygame.display.flip()

    def draw_screen_not_clicked(self):
        """Funktio piirtämään näyttö kun ei ole valittu pelattavan
        tietokonetta vastaan"""
        self.screen.fill(self.bg_color)
        self.draw_text("VALITSE VASTUSTAJA:", 100, 100, 1)
        self.draw_button(self.multiplayer_button)
        self.draw_text("KAVERI", 240, 500, 1)
        self.draw_button(self.singleplayer_button)
        self.draw_text("TIETOKONE", 225, 275, 1)
        pygame.display.flip()

    def draw_levels(self):
        """Funktio piirtämään vaikeustasopainikkeet
        tietokonetta vastaan ja niihin testit"""
        self.draw_button(self.easy_button)
        self.draw_text("HELPPO", 73, 285, 2)
        self.draw_button(self.medium_button)
        self.draw_text("KESKITASO", 275, 285, 2)
        self.draw_button(self.hard_button)
        self.draw_text("VAIKEA", 520, 285, 2)
