from tokenize import single_quoted
from tracemalloc import start
from modules import mm_ab
from modules.singleplayer import SinglePlayer
from modules import gameplay
import statistics
import random
import time
EASY = 2
MEDIUM = 4
HARD = 6
def performance_test(play, amo):
    print()
    print("laskelmoidaan kaikkea kivaa....")
    print()
    times = []
    for _ in range (amo):
        board = create_board()
        play.board = board
        start_time = time.time()
        play.ai_turn()
        end_time = time.time()
        times.append(end_time - start_time)
    mean_of_times = statistics.mean(times)
    print(f"Satunnaisessa pelitilanteessa tietokone pohdiskeli siirtoa {amo} sekunnin verran")
    print(f"Aikojen keskiarvo oli {mean_of_times} sekuntia")

def create_board():
    cre = False
    while not cre:
        board = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
        for i in range(11):
            if i % 2 == 0:
                y = -1
                while y == -1:
                    x = random.randint(0,6)
                    y = mm_ab.low_free(board, x)
                board [y][x] = 1
            else:
                y = 1
                while y == -1:
                    x = random.randint(0,6)
                    y = mm_ab.low_free(board, x)
                board[y][x] = 2
        if gameplay.check_win(board) == 0:
            cre = True
    return board

easy_play = SinglePlayer(EASY)
medium_play = SinglePlayer(MEDIUM)
hard_play = SinglePlayer(HARD)

while True:
    level = input("Valitse vaikeustaso jota testataan, jossa h = helppo, m = medium, v = vaikea ja q = lopeta")
    if level == "q":
        break
    print()
    amo = int(input("Otoksen suuruus (satunnainen luku):"))
    if level == "h":
        performance_test(easy_play, amo)
    if level == "m":
        performance_test(medium_play, amo)
    if level == "v":
        performance_test(hard_play, amo)
