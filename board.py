from turtle import screensize
import pygame
import numpy as np
import draw

class gameBoard():
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 800
        self.BOARD_ROWS = 3
        self.BOARD_COLS = 3
        self.background_colour=(200,120,149)
        self.boardSlots = np.zeros( (self.BOARD_ROWS, self.BOARD_COLS))
        self.screen = None
        self.gameOver = False
        

    def initBoard(self):

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        pygame.display.set_caption('Tik Tac Toe')

        self.screen.fill(self.background_colour)

        draw.drawingMethods.drawLines(None,self.screen)

        return self.screen

    
    def available_square(self,row, col):
        return self.boardSlots[row][col] == 0


    def mark_square(self,row, col, player):
        self.boardSlots[row, ][col] = player


    def is_board_full(self):
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                if self.boardSlots[row][col] == 0:
                    return False
        return True 