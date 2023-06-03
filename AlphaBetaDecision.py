#NAME: Shivani Panchiwala
#UTA ID: 1001982478


from MaxConnect4Game import *
from copy import deepcopy

def AlphaBetaDecision(state):
    lstGames = []
    # print minusInfinite, infinite
    for a,s in Successor(state):
        v = Min_Value(s, -2147483647, 2147483648, deepcopy(state.depthLimt))
        lstGames.append((a, v))
    # print lstGames
    finalSelection = []
    i = 0
    for game in lstGames:
        if i == 0:
            finalSelection = game
            i += 1
            continue
        if game[1] > finalSelection[1]:
            finalSelection = game
        i += 1
    
    return finalSelection[0], finalSelection[1]

def Max_Value(state, alpha, beta, depth):
    if state.checkPieceCount() == 41 or depth == 1:
        state.countScore()
        return state.score_Eval()
    v = -2147483647
    # print 'Max:\n','alpha: ', alpha, 'beta: ', beta, 'v: ', v
    for a,s in Successor(state):
        v = max(v, Min_Value(s, alpha, beta, deepcopy(depth - 1)))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def Min_Value(state, alpha, beta, depth):
    if state.checkPieceCount() == 41 or depth == 1:
        state.countScore()
        return state.score_Eval()
    v = 2147483648
    # print 'Min:\n','alpha: ', alpha, 'beta: ', beta, 'v: ', v
    for a,s in Successor(state):
        v = min(v, Max_Value(s, alpha, beta, deepcopy(depth - 1)))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def Successor(state):
    lstGames = []
    if state.currentTurn == 1:
        ct = 2
    else:
        ct = 1
    for j in range(7):
        newGame = maxConnect4Game()
        newGame.gameBoard = deepcopy(state.gameBoard)
        newGame.currentTurn = ct
        if newGame.playPiece(j):
            lstGames.append((j, newGame))
    return lstGames
