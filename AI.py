from copy import deepcopy

from utility import check_win,checkWinNoDraw,checkWinNoPlayer
import board
import draw
import math
import sys

class AI():
    def __init__(self):
        pass

    def getCoords(self, gameBoard:board.gameBoard,player):
        print(gameBoard.boardSlots[0][0])
        print(gameBoard.boardSlots[0][1])
        print(gameBoard.boardSlots[0][2])
        if (player==1):
            (m, qx, qy) = self.max_alpha_beta(gameBoard.boardSlots,player,-2, 2)
            return (m,qx,qy)
        elif (player==2): #X
            (m, px, py) = self.min_alpha_beta(gameBoard.boardSlots,player,-2, 2)
            return (m,px,py)
           

    def gameEnded(self,gameBoard):
        return checkWinNoPlayer(gameBoard)
        
    def getPossibleMoves(self,gameBoard):
        moves = []
        for i in range(3):
            for j in range(3):
                if gameBoard[i][j]==0:
                    moves.append([i,j])

        return moves

    def isBoardFull(self,gameBoard):
        for i in range(3):
            for j in range(3):
                if gameBoard[i][j]==0:
                    return False
        return True
    
    def max_alpha_beta(self, gameBoard, player, alpha, beta):
        maxv = -2
        px = None
        py = None

        result = self.gameEnded(gameBoard)

        if result == -1:
            return (-1, 0, 0)
        elif result == 1:
            return (1, 0, 0)
        elif result == 0:
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if gameBoard[i][j] == 0 and [i,j] not in self.getPossibleMoves(gameBoard):
                    gameBoard[i][j] = player
                    (m, min_i, in_j) = self.min_alpha_beta(gameBoard,player,alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = 0

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)

    def min_alpha_beta(self,gameBoard,player, alpha, beta):
        minv = 2

        qx = None
        qy = None

        result = self.gameEnded(gameBoard)

        if result == -1:
            return (-1, 0, 0)
        elif result == 1:
            return (1, 0, 0)
        elif result == 0:
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if gameBoard[i][j] == 0  and [i,j] not in self.getPossibleMoves(gameBoard):
                    gameBoard[i][j] = player
                    (m, max_i, max_j) = self.max_alpha_beta(gameBoard,player,alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = 0

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)

