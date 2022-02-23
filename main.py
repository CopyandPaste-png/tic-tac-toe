import os
import sys
import pygame
import numpy as np
from tkinter import *
import sqlite3

pygame.init()

WIDTH = 600
HEIGHT = 600

LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
#R, G, B

RED = (255,255,255)
background_colour = (200,120,149)
LINE_COLOUR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tik Tac Toe')
screen.fill(background_colour)

# Board
board = np.zeros( (BOARD_ROWS, BOARD_COLS))

# Draws --- ||| lines
def draw_lines():
    # 1 horizontal line
    pygame.draw.line( screen, LINE_COLOUR, (0,200), (600,200), LINE_WIDTH)
    # 2 horizontal line
    pygame.draw.line( screen, LINE_COLOUR, (0,400), (600,400), LINE_WIDTH)

    # 1 vertical line
    pygame.draw.line( screen, LINE_COLOUR, (200,0), (200,600), LINE_WIDTH)
    # 2 vertical line
    pygame.draw.line( screen, LINE_COLOUR, (400,0), (400,600), LINE_WIDTH)
    # 3 vertical line
    pygame.draw.line( screen, LINE_COLOUR, (600,0), (600,600), LINE_WIDTH)
# draws the circle of 1/2 on click

# Draws X/O
def draw_figure():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] == 1: #if the player clicks on the board the circle is draw using the code below
                pygame.draw.circle( screen, RED, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line( screen, RED, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line( screen, RED, (col * 200 + SPACE, row * 200 +  SPACE), (col * 200 + 200 - SPACE, row * 200+ 200 - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row, ][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

#Win conditions
def draw_horizontal_winning_line(row, player):
    posY =  row * 200 + 100

    if player == 1:
        colour = RED
    elif player == 2:
        colour = RED

    pygame.draw.line(screen, colour, (15, posY),(WIDTH - 15, posY),15)
    
def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        colour = RED
    if player == 2:
        colour = RED

    pygame.draw.line(screen, colour, (posX, 15),(posX, WIDTH - 15),15)

def draw_asc_diagonal(player):
    if player == 1:
        colour = RED
    if player ==2:
        colour = RED

    pygame.draw.line(screen, colour, (15, HEIGHT - 15),(WIDTH - 15,15),15)

def draw_desc_diagonal(player):
    if player == 1:
        colour = RED
    elif player == 2:
        colour = RED

    pygame.draw.line(screen, colour,(15,15),(HEIGHT - 15,HEIGHT - 15),15)

#Checks win
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board [row][2] == player:
            draw_horizontal_winning_line(row, player)

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False

def restart():
    screen.fill(background_colour)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

def main():
    draw_lines()

    player = 1
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = player % 2 + 1

                    draw_figure()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    game_over = False
            
        pygame.display.update()


if __name__=="__main__":
    main()