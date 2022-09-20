"""Moduuli, joka sisältää tekoälyn"""
from modules import gameplay
"""ORDER on lista arvoja joidenka järjestyksessä on parasta käydä
läpi pelilaudan sarakkeet"""
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
        for x in ORDER:
            y = low_free(board, x)
            if y == -1:
                continue
            board[y][x] = 2
            score = minimax(board, False, depth - 1, alpha, beta)
            board[y][x] = 0
            top_score = max(top_score, score)
            alpha = max(alpha, score)  
        return top_score
    if not max:
        top_score = INF
        for x in ORDER:
            y = low_free(board, x)
            if y == -1:
                continue
            board[y][x] = 1
            score = minimax(board, True, depth - 1, alpha, beta)
            board[y][x] = 0
            top_score = min(top_score, score)
            beta = min(beta, score)
        return top_score

def best_move_check(board, depth):
    """Funktio, joka palauttaa parhaan reitin.
    Kutsuu minimax algoritmia."""
    action = (-1, -1)
    top_score = -INF
    for x in ORDER:
        y = low_free(board, x)
        if y == -1:
            continue
        board[y][x] = 2
        score = minimax(board, False, depth, -INF, INF)
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
    """Palauttaa pelitilanteen arvosanan
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
