import pygame

class Menu_UI:

    def __init__(self):
        self.screen_height = 700
        self.screen_width = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.singleplayer_button = pygame.Rect(100, 225, 500, 150)
        self.multiplayer_button = pygame.Rect(100, 450, 500, 150)
        self.easy_button = pygame.Rect(50,240,150,120)
        self.medium_button = pygame.Rect(275,240,150,120)
        self.hard_button = pygame.Rect(500,240,150,120)
        self.bg_color = (255, 0, 255)
        self.button_color = (255, 255, 0)

    def setup(self):
        pygame.display.set_caption("CONNECT FOUR")
        self.font = pygame.font.SysFont("comicsansms", 45, 1)
        self.font2 = pygame.font.SysFont("comicsansms", 25, 1)

    def reset_caption(self):
        pygame.display.set_caption("CONNECT FOUR")

    def draw_text(self, text, x_value, y_value, font):
        if font == 1:
            text_area = self.font.render(text, True, (255, 255, 255))
        if font == 2:
            text_area = self.font2.render(text, True, (255, 255, 255))
        self.screen.blit(text_area, (x_value, y_value))

    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)

    def draw_screen_if_clicked(self):
        self.screen.fill(self.bg_color)
        self.draw_text("VALITSE VASTUSTAJA:", 100, 100, 1)
        self.draw_button(self.multiplayer_button)
        self.draw_text("KAVERI", 240, 500, 1)
        self.draw_levels()
        pygame.display.flip()

    def draw_screen_not_clicked(self):
        self.screen.fill(self.bg_color)
        self.draw_text("VALITSE VASTUSTAJA:", 100, 100, 1)
        self.draw_button(self.multiplayer_button)
        self.draw_text("KAVERI", 240, 500, 1)
        self.draw_button(self.singleplayer_button)
        self.draw_text("TIETOKONE", 225, 275, 1)
        pygame.display.flip()

    def draw_levels(self):
        self.draw_button(self.easy_button)
        self.draw_text("HELPPO", 73, 285, 2)
        self.draw_button(self.medium_button)
        self.draw_text("KESKITASO", 275, 285, 2)
        self.draw_button(self.hard_button)
        self.draw_text("VAIKEA", 520, 285, 2)