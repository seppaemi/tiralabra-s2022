"""Moduuli, joka sisältää tekoälyn"""
import numpy
from modules import gameplay
ORDER = [3,2,4,1,5,0,6]
INF = 10000000

def minimax(board, max, depth, alpha, beta):
    """Toteuttaa minimax algoritmin
    """
    if depth == 0:
        return board_calc(board)
    winner = gameplay.check_win(board)
    if winner == 2:
        return 10000
    if winner == 1:
        return -1000
    if max:
        top_score = -INF
        for x_axis in ORDER:
            y_axis = low_free(board, x_axis)
            if y_axis == -1:
                continue
            board[y_axis][x_axis] = 2
            score = minimax(board, False, depth - 1, alpha, beta)
            board[y_axis][x_axis] = 0
            top_score = max(top_score, score)
            alpha = max(alpha, score)  
        return top_score
    if not max:
        top_score = INF
        for x_axis in ORDER:
            y_axis = low_free(board, x_axis)
            if y_axis == -1:
                continue
            board[y_axis][x_axis] = 1
            score = minimax(board, True, depth - 1, alpha, beta)
            board[y_axis][x_axis] = 0
            top_score = min(top_score, score)
            beta = min(beta, score)
        return top_score

def best_move_check(board, depth):
    """Funktio, joka palauttaa parhaan reitin.
    Kutsuu minimax algoritmia."""
    action = (-1, -1)
    top_score = -INF
    for x_axis in ORDER:
        y_axis = low_free(board, x_axis)
        if y_axis == -1:
            continue
        board[y_axis][x_axis] = 2
        score = minimax(board, False, depth, -INF, INF)
        board[y_axis][x_axis] = 0
        if score > top_score:
            top_score = score
            action =  (y_axis,x_axis)
    return action

def low_free(board, x_axis):
    """Etsii sarakkeen x_axis pohjimmaisen vapaan ruudun y_axis"""
    for y_axis in range(5,-1,-1):
        if board[y_axis][x_axis] == 0:
            return y_axis
    return -1

def board_calc(board):
    """Palauttaa pelitilanteelle arvosanan
    """
    score = 0
    score += check_vert(board)
    if score >= 10000 or score <= -1000:
        return score
    score += check_hor(board)
    if score >= 10000 or score <= -1000:
        return score
    score += check_diag_up(board)
    if score >= 10000 or score <= -1000:
        return score
    score += check_diag_down(board)
    return score

def check_vert(board):
    """Arvosana pystyriveiltä."""
    grade_change = 0
    n_board = numpy.array(board)
    for x_axis in ORDER:
        col = n_board[:,x_axis]
        for y_axis in range(5,2,-1):
            vertical=[col[y_axis-3],col[y_axis-2],col[y_axis-1],col[y_axis]]
            if count_four(vertical) != 0:
                return count_four(vertical)
            grade_change += count_three(vertical)
    return grade_change

def check_hor(board):
    """Arvosana vaakariviltä"""
    grade_change = 0
    for y_axis in range(5,-1,-1):
        row = board[y_axis][:]
        for x_axis in range(6,2,-1):
            horisontal = [row[x_axis-3],row[x_axis-2],row[x_axis-1],row[x_axis]]
            if count_four(horisontal) != 0:
                return count_four(horisontal)
            grade_change += count_three(horisontal)
    return grade_change

def check_diag_up(board):
    """Arvosana ylös viistoon"""
    grade_change = 0
    for y_axis in range(5,2,-1):
        for x_axis in range(3,-1,-1):
            u_diagonal = [board[y_axis][x_axis],board[y_axis-1][x_axis+1],
                        board[y_axis-2][x_axis+2],board[y_axis-3][x_axis+3]]
            if count_four(u_diagonal) != 0:
                return count_four(u_diagonal)
            grade_change += count_three(u_diagonal)
    return grade_change

def check_diag_down(board):
    """Arvosana alas viistoon"""
    grade_change = 0
    for y_axis in range(5,2,-1):
        for x_axis in range(3,7):
            d_diagonal = [board[y_axis-3][x_axis-3], board[y_axis-2][x_axis-2],
                        board[y_axis-1][x_axis-1], board[y_axis][x_axis]]
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
