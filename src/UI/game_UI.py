"""Moduuli jossa on luokka Game_UI"""
import pygame
from load_image import load_image


class Game_UI:
    """Luokka joka vastaa koko pelin käyttöliittymästä
    Attributes:
    place_size: kertoo pelilaudan koon pikseleinä
    screen_height: kertoo ikkunna korkeuden pikseleinä
    screen_width: kertoo ikkunan leveyden pikseleinä
    screen: Tähän on tallennettu peli-ikkuna
    red_piece: tähän on tallennettu kuva punaisesta pelinappulasta
    green_piece: tähän on tallennettu kuva vihreästä pelinappulasta
    empty: tähän on tallennettu kuva tyhjästä pelinappulasta"""
    def __init__(self):
        """Luokan konstruktori"""
        self.place_size = 100
        self.screen_height = self.place_size * 7
        self.screen_width = self.place_size * 7
        self.screen = None
        self.red_piece = load_image("red.png")
        self.green_piece = load_image("green.png")
        self.green_played = load_image("green_played.png")
        self.red_played = load_image("red_played.png")
        self.empty = load_image("empty.png")

    def game_UI_setup(self, title):
        """Tekee käyttöliittymän alkutoimet """
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption(f"CONNECT FOUR - {title}")
        self.font = pygame.font.SysFont("Helvetica", 45, 1)

    def draw_victory(self, green_won, red_won):
        """Funktio joka kirjoittaa tekstin voittajasta"""
        if green_won:
            green_text = self.font.render(
                "VIHREÄ VOITTI!", True, (255, 255, 0))
            self.screen.blit(green_text, (150, 25))
        if red_won:
            red_text = self.font.render("PUNAINEN VOITTI!", True, (255, 0, 0))
            self.screen.blit(red_text, (150, 25))

    def draw_tie(self):
        """Funktio joka kirjoittaa tekstin tasapelistä"""
        tie_text = self.font.render("TASAPELI", True, (255, 255, 255))
        self.screen.blit(tie_text, (250, 25))

    def draw_piece(self, ai, green_turn, mouse_pos):
        """Funktio, joka piirtää pelinappulan hiiren kohdalle"""
        x = mouse_pos[0]
        x -= 50
        if x < 0:
            x = 0
        if x >= 600:
            x = 600
        if green_turn:
            self.screen.blit(self.green_piece, (x, 0))
        else:
            if ai:
                ai_txt = self.font.render("laskelmoidaan siirtoa", True, (255, 0, 0))
                self.screen.blit(ai_txt, (135,25))
            else:
                self.screen.blit(self.red_piece, (x, 0))

    def correct_image(self, place):
        """Funktio, joka valitsee oikean kuvan asetetulle pelimerkille"""
        if place == 0:
            return self.empty
        if place == 1:
            return self.green_played
        if place == 2:
            return self.red_played

    def draw_screen(self, board, game_over, tie_game, green_won,
                    red_won, ai, green_turn, mouse_pos):
        """Funktio, joka piirtää näytön"""
        self.screen.fill((22, 8, 91))
        for y_value in range(6):
            for x_value in range(7):
                image = self.correct_image(board[y_value][x_value])
                self.screen.blit(
                    image, (x_value*self.place_size, y_value*self.place_size+100))
        if game_over:
            if not tie_game:
                self.draw_victory(green_won, red_won)
            else:
                self.draw_tie()
        if not game_over:
            self.draw_piece(ai, green_turn, mouse_pos)
            pygame.display.update()
        pygame.display.flip()
