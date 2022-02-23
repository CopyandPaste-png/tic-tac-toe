import pygame
import numpy as np
import pygame
import sys

class drawingMethods():
    def __init__(self) -> None:
            pass

    DEFAULTCOLOUR = (255,255,255) #red
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55
    LINE_COLOUR = (0, 0, 0)
    LINE_WIDTH = 15
    WIDTH = 600
    HEIGHT = 600


    def drawLines(self,screen,lineColour=LINE_COLOUR,lineWidth = LINE_WIDTH):
        #drawing horizontal lines
        
        for i in range(1,3):

            pygame.draw.line( screen,lineColour, (0,200*i), (600,200*i), lineWidth)


        #pygame.draw.line( screen, self.LINE_COLOUR, (0,400), (600,400), self.LINE_WIDTH)

        #drawing vertical lines
        for i in range(1,4):
            pygame.draw.line( screen, lineColour, (200*i,0), (200*i,600), lineWidth)
    
    #Win conditions
    def draw_horizontal_winning_line(self,row, screen, colour=DEFAULTCOLOUR, width=WIDTH):
        posY =  row * 200 + 100
        pygame.draw.line(screen, colour, (15, posY),(width - 15, posY),15)


    def draw_vertical_winning_line(self,col, screen,colour=DEFAULTCOLOUR,width=WIDTH):
        posX = col * 200 + 100
        pygame.draw.line(screen, colour, (posX, 15),(posX, width - 15),15)


    def draw_asc_diagonal(self,screen,colour=DEFAULTCOLOUR,height=HEIGHT,width=WIDTH):
        pygame.draw.line(screen, colour, (15, height - 15),(width - 15,15),15)


    def draw_desc_diagonal(self,screen,colour=DEFAULTCOLOUR,height=HEIGHT):
        pygame.draw.line(screen, colour,(15,15),(height - 15,height - 15),15)


    def drawCircle(self,gameBoard,screen,colour=DEFAULTCOLOUR,circleRad=CIRCLE_RADIUS,circleWidth=CIRCLE_WIDTH,circleCrossWidth=CROSS_WIDTH,space=SPACE):
        for row in range (3):
            for col in range (3):
                if gameBoard[row][col] == 1: #if the player clicks on the board the circle is draw using the code below
                    pygame.draw.circle( screen, colour, (int(col * 200 + 100), int(row * 200 + 100)), circleRad, circleWidth)

                elif gameBoard[row][col] == 2:
                    pygame.draw.line( 
                        screen, 
                        colour, 
                        (col * 200 + space, row * 200 + 200 - space), 
                        (col * 200 + 200 - space, row * 200 + space),
                        circleCrossWidth)

                    pygame.draw.line( 
                        screen,
                        colour,
                        (col * 200 + space, row * 200 + space), 
                        (col * 200 + 200 - space, row * 200+ 200 - space),
                        circleCrossWidth)



class gameBoard():
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 800
        self.BOARD_ROWS = 3
        self.BOARD_COLS = 3
        self.background_colour=(200,120,149)
        self.boardSlots = np.zeros( (self.BOARD_ROWS, self.BOARD_COLS))
        

    def initBoard(self):
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        pygame.display.set_caption('Tik Tac Toe')

        screen.fill(self.background_colour)

        drawingMethods.drawLines(None,screen)

        return screen

    
    def available_square(self,row, col):
        return self.boardSlots[row][col] == 0


    def mark_square(self,row, col, player):
        self.boardSlots[row, ][col] = player


class gameWrapper():
    def __init__(self):
        self.gameBoard = gameBoard()
        self.draw = drawingMethods()
        self.BOARD_ROWS = 3
        self.BOARD_COLS = 3

    
    def start(self):
        
        pygame.init()
        screen = self.gameBoard.initBoard()

        player = 1
        gameOver = False

        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    clicked_row = int(mouseY // 200)
                    clicked_col = int(mouseX // 200)

                    if self.gameBoard.available_square(clicked_row, clicked_col):
                        self.gameBoard.mark_square(clicked_row, clicked_col, player)
                        if self.check_win(screen,player):
                            gameOver = True
                        player = player % 2 + 1

                        self.draw.drawCircle(self.gameBoard.boardSlots,screen)

                    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()  
                
            

    #Checks win
    def check_win(self,gameScreen,player):
        tempGameBoard = self.gameBoard.boardSlots

        for col in range(self.BOARD_COLS):
            if tempGameBoard[0][col] == player and tempGameBoard[1][col] == player and tempGameBoard[2][col] == player:
                self.draw.draw_vertical_winning_line(col,gameScreen)
                return True

        for row in range(self.BOARD_ROWS):
            if tempGameBoard[row][0] == player and tempGameBoard[row][1] == player and tempGameBoard[row][2] == player:
                self.draw.draw_horizontal_winning_line(row, gameScreen)


        if tempGameBoard[2][0] == player and tempGameBoard[1][1] == player and tempGameBoard[0][2] == player:
            self.draw.draw_asc_diagonal(gameScreen)

            return True
        elif tempGameBoard[0][0] == player and tempGameBoard[1][1] == player and tempGameBoard[2][2] == player:
            self.draw.draw_desc_diagonal(gameScreen)
            return True
        return False
    
    

def main():
    gw = gameWrapper()
    gw.start()


if __name__=="__main__":
    main()