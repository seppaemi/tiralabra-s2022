"""Moduuli, joka sisältää peliin ja 
sen toimintaan liittyviä funktioita
"""
import numpy
"""ORDER kuvaa parhaimman järjestyksen 
läpikäydä pelilaudan sarakkeet"""
ORDER = [3, 2, 4, 1, 5, 0, 6]


def check_tie(board):
    """Tarkastaa onko pelilauta täynnä ja 
    palauttaa boolean arvon siitä riippuen"""
    full = True
    for x in range(0, 7):
        if not check_column_full(board, x):
            full = False
    return full


def check_if_four(line):
    """Tarkastaakummalla pelaajalla neljä 
    rivissä ja palauttaa lukuarvon sen 
    mukaan tai -1 jos ei kumpikaan"""
    if line.count(1) == 4:
        return 1
    if line.count(2) == 4:
        return 2
    return -1


def check_win(board):
    """Tarkastaa kumpi voitti ja palauttaa
    lukuarvon sen mukaan tai 0 jos ei kumpikaan"""
    hor = check_horizontal(board)
    vert = check_vertical(board)
    up_dia = check_up_diagonal(board)
    do_dia = check_down_diagonal(board)
    if hor == 1 or vert == 1 or up_dia == 1 or do_dia == 1:
        return 1
    if hor == 2 or vert == 2 or up_dia == 2 or do_dia == 2:
        return 2
    return 0


def check_horizontal(board):
    """Tarkistaa vaakariviltä neljä samaa"""
    for y in range(5, -1, -1):
        row = board[y][:]
        for x in range(6, 2, -1):
            hor = [row[x-3], row[x-2], row[x-1], row[x]]
            if check_if_four(hor) == 2:
                return 2
            if check_if_four(hor) == 1:
                return 1
    return 0


def check_vertical(board):
    """Tarkistaa pystyriviltä neljä samaa"""
    n_board = numpy.array(board)
    for x in ORDER:
        col = n_board[:, x]
        for y in range(5, 2, -1):
            vert = [col[y-3], col[y-2], col[y-1], col[y]]
            if check_if_four(vert) == 2:
                return 2
            if check_if_four(vert) == 1:
                return 1
    return 0


def check_up_diagonal(board):
    """Tarkistaa neljä samaa ylöspäin viistoon"""
    for y in range(5, 2, -1):
        for x in range(3, -1, -1):
            up_dia = [board[y][x], board[y-1][x+1],
                      board[y-2][x+2], board[y-3][x+3]]
            if check_if_four(up_dia) == 2:
                return 2
            if check_if_four(up_dia) == 1:
                return 1
    return 0


def check_down_diagonal(board):
    """tarkistaa neljä samaa alaspäin viistoon"""
    for y in range(5, 2, -1):
        for x in range(3, 7):
            do_dia = [board[y-3][x-3], board[y-2][x-2],
                      board[y-1][x-1], board[y][x]]
            if check_if_four(do_dia) == 2:
                return 2
            if check_if_four(do_dia) == 1:
                return 1
    return 0


def check_column_full(board, x):
    """Tarkistaa onko sarake x täynnä ja
    palauttaa True jos on ja False jos ei"""
    if board[0][x] != 0:
        return True
    return False
