"""Moduuli, joka sisältää tekoälyn"""
import numpy
from modules import gameplay
ORDER = [3,2,4,1,5,0,6]
INF = 10000000

def minmax(board, max_bool, depth, alpha, beta):
    """Toteuttaa minmax algoritmin
    """
    if depth == 0:
        return board_calc(board)
    winner = gameplay.check_win(board)
    if winner == 2:
        return 10000
    if winner == 1:
        return -10000
    if max_bool:
        top_score = -INF
        for x in ORDER:
            y = low_free(board, x)
            if y == -1:
                continue
            board[y][x] = 2
            score = minmax(board, False, depth - 1, alpha, beta)
            board[y][x] = 0
            top_score = max(top_score, score)
            alpha = max(alpha, score)
            if beta <=alpha:
                break
        return top_score
    if not max_bool:
        top_score = INF
        for x in ORDER:
            y = low_free(board, x)
            if y == -1:
                continue
            board[y][x] = 1
            score = minmax(board, True, depth - 1, alpha, beta)
            board[y][x] = 0
            top_score = min(top_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return top_score

def best_move_check(board, depth):
    """Funktio, joka palauttaa parhaan reitin.
    Kutsuu minmax algoritmia."""
    action = (-1, -1)
    top_score = -INF
    for x in ORDER:
        y = low_free(board, x)
        if y == -1:
            continue
        board[y][x] = 2
        score = minmax(board, False, depth, -INF, INF)
        board[y][x] = 0
        if score > top_score:
            top_score = score
            action =  (y,x)
    return action

def low_free(board, x):
    """Etsii sarakkeen x pohjimmaisen vapaan ruudun y"""
    for y in range(5,-1,-1):
        if board[y][x] == 0:
            return y
    return -1

def board_calc(board):
    """Palauttaa pelitilanteelle arvosanan
    """
    score = 0
    score += check_vert(board)
    if score >= 10000 or score <= -10000:
        return score
    score += check_hor(board)
    if score >= 10000 or score <= -10000:
        return score
    score += check_diag_up(board)
    if score >= 10000 or score <= -10000:
        return score
    score += check_diag_down(board)
    return score

def check_vert(board):
    """Arvosana pystyriveiltä."""
    grade_change = 0
    n_board = numpy.array(board)
    for x in ORDER:
        col = n_board[:,x]
        for y in range(5,2,-1):
            vertical=[col[y-3],col[y-2],col[y-1],col[y]]
            if count_four(vertical) != 0:
                return count_four(vertical)
            grade_change += count_three(vertical)
    return grade_change

def check_hor(board):
    """Arvosana vaakariviltä"""
    grade_change = 0
    for y in range(5,-1,-1):
        row = board[y][:]
        for x in range(6,2,-1):
            horisontal = [row[x-3],row[x-2],row[x-1],row[x]]
            if count_four(horisontal) != 0:
                return count_four(horisontal)
            grade_change += count_three(horisontal)
    return grade_change

def check_diag_up(board):
    """Arvosana ylös viistoon"""
    grade_change = 0
    for y in range(5,2,-1):
        for x in range(3,-1,-1):
            u_diagonal = [board[y][x],board[y-1][x+1],
                        board[y-2][x+2],board[y-3][x+3]]
            if count_four(u_diagonal) != 0:
                return count_four(u_diagonal)
            grade_change += count_three(u_diagonal)
    return grade_change

def check_diag_down(board):
    """Arvosana alas viistoon"""
    grade_change = 0
    for y in range(5,2,-1):
        for x in range(3,7):
            d_diagonal = [board[y-3][x-3], board[y-2][x-2],
                        board[y-1][x-1], board[y][x]]
            if count_four(d_diagonal) != 0:
                return count_four(d_diagonal)
            grade_change += count_three(d_diagonal)
    return grade_change

def count_three(line):
    """Laskee riville arvosanan, sen perusteella
    onko siinä jo kolme"""
    if line == [0,1,1,1] or line == [1,1,1,0]:
        return -100
    if line == [0,2,2,2] or line == [2,2,2,0]:
        return 10
    return 0

def count_four(line):
    """Tarkistaa onko voittoa saadussa listassa
    """
    if line == [1,1,1,1]:
        return -1000
    if line == [2,2,2,2]:
        return 10000
    return 0
