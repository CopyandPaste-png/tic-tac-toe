from audioop import cross
import pygame

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
                if gameBoard.boardSlots[row][col] == 1: #if the player clicks on the board the circle is draw using the code below
                    pygame.draw.circle( screen, colour, (int(col * 200 + 100), int(row * 200 + 100)), circleRad, circleWidth)

                elif gameBoard.boardSlots[row][col] == 2:
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
 