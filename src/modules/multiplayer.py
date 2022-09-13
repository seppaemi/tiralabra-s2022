import pygame
from modules import gameplay
from UI.game_UI import Game_UI
class Play:
    def __init__(self):
        self.ui = Game_UI()
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False
        self.red_win = False
        self.green_win = False
        self.end_tie = False
        self.game_over = False
        self.green_turn = True
        self.ai = False
        self.mouse_pos = (0,0)
        self.title = "Kaveria vastaan"
       
    def run(self):
        while True:
            pygame.init()
            self.ui.game_UI_setup(self.title)
            self.running = True
            self.gameloop()
            break

    def restart(self):
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = True
        self.red_win = False
        self.green_win = False
        self.end_tie = False
        self.game_over = False
        self.green_turn = True

    def full_column(self, x):
        return gameplay.check_column_full(self.board, x)

    def green_win(self):
        self.green_win = True
        self.game_over = True

    def red_wins(self):
        self.red_win = True
        self.game_over = True

    def check_for_win(self):
        result = gameplay.check_win(self.board)
        if result == 1:
            self.green_win()
        if result ==2:
            self.red_wins()

    def check_for_tie(self):
        if gameplay.check_tie(self.board):
            self.tie()

    def tie(self):
        self.game_over = True
        self.end_tie = True

    def def_mouse(self, pos):
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
                    self.def_mouse(pos)
            if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = pygame.mouse.get_pos()

    def gameloop(self):
        while self.running:
            self.event_check()
            self.ui.draw_screen(self.board, self.game_over, 
                            self.end_tie, self.green_win,
                            self.red_win, self.ai,
                            self.green_turn, self.mouse_pos)