from numpy import place
import draw

def check_win(gameBoard,screen,player,BOARD_COLS=3,BOARD_ROWS=3):
    
    drawingMethod =draw.drawingMethods()

    tempGameBoard = gameBoard

    for col in range(BOARD_COLS):
        if tempGameBoard[0][col] == player and tempGameBoard[1][col] == player and tempGameBoard[2][col] == player:
            drawingMethod.draw_vertical_winning_line(col,screen)
            return True

    for row in range(BOARD_ROWS):
        if tempGameBoard[row][0] == player and tempGameBoard[row][1] == player and tempGameBoard[row][2] == player:
            drawingMethod.draw_horizontal_winning_line(row, screen)


    if tempGameBoard[2][0] == player and tempGameBoard[1][1] == player and tempGameBoard[0][2] == player:
        drawingMethod.draw_asc_diagonal(screen)
        return True

    elif tempGameBoard[0][0] == player and tempGameBoard[1][1] == player and tempGameBoard[2][2] == player:
        drawingMethod.draw_desc_diagonal(screen)
        return True

    return False


def checkWinNoDraw(gameBoard,player,BOARD_COLS=3,BOARD_ROWS=3):
    tempGameBoard = gameBoard
    for col in range(BOARD_COLS):
        if tempGameBoard[0][col] == player and tempGameBoard[1][col] == player and tempGameBoard[2][col] == player:
            return True
    for row in range(BOARD_ROWS):
        if tempGameBoard[row][0] == player and tempGameBoard[row][1] == player and tempGameBoard[row][2] == player:
            return True
    if tempGameBoard[2][0] == player and tempGameBoard[1][1] == player and tempGameBoard[0][2] == player:
        return True
    elif tempGameBoard[0][0] == player and tempGameBoard[1][1] == player and tempGameBoard[2][2] == player:
        return True

    return False


def checkWinNoPlayer(gameBoard):
    player1 = 1 #O
    player2 = 2 #X

    if checkWinNoDraw(gameBoard,player1):
        return 1
    elif checkWinNoDraw(gameBoard,player2):
        return -1
    return 0