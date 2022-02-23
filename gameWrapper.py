from importlib_metadata import flake8_bypass
import board
import pygame
import sys
import draw
import AI
from utility import check_win

class gameWrapper():
    def __init__(self):
        self.gameBoard = board.gameBoard()
        self.draw = draw.drawingMethods()
        self.AI = AI.AI()
        self.BOARD_ROWS = 3
        self.BOARD_COLS = 3
        self.multiplayer = False
        self.AIturn = True

    
    def start(self):
        
        pygame.init()
        self.gameBoard.initBoard()

        player = 1

        run = True

        while run:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                print(self.gameBoard.boardSlots)
              
                
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and not self.gameBoard.gameOver and self.multiplayer==False:
                    

                    
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    clicked_row = int(mouseY // 200)
                    clicked_col = int(mouseX // 200)

                    if (self.gameBoard.available_square(clicked_row, clicked_col) and self.gameBoard.gameOver==False):
                        self.gameBoard.mark_square(clicked_row, clicked_col, player)
                        if check_win(self.gameBoard.boardSlots,self.gameBoard.screen,player):
                            self.gameBoard.gameOver = True
                        
                        self.draw.drawCircle(self.gameBoard,self.gameBoard.screen)
                        
                        AICoords = self.AI.getCoords(self.gameBoard,player%2+1)

                        print(AICoords[1],AICoords[2])

                        #self.gameBoard.mark_square(AICoords[1],AICoords[2],player%2+1)

                        #self.draw.drawCircle(self.gameBoard,self.gameBoard.screen)

                        player = player %2 +1
                        
                    


                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()  

