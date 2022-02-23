from click import secho
import pygame
pygame.init()

#Screen
size = width, height = 1280, 720 #Make sure background image is same size
screen = pygame.display.set_mode(size)

done = False

#Time Info
Time = 0
Second = 0
Minute = 0
Day = 0
counter=0

#Colour
Black = (0,0,0)
White = (255, 255, 255)

#Fonts
Font = pygame.font.SysFont("Trebuchet MS", 25)

#Hour
timeFont = Font.render("{0:02}:{0:02}".format(Second,Minute),1, Black) #zero-pad hours to 2 digits
timeFont=timeFont.get_rect()
timeFont.center=(985,20)

Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # fired once every second

screen.fill(White)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == CLOCKTICK: # count up the clock
            #Timer
            secondText = ""
            
            Second=Second+1
            if Second == 60:
                Minute=Minute+1
                Second=0

            # redraw time
            screen.fill(White)
            
            if Second < 10:
                secondText = "0"+str(int(Second))
            else:
                secondText = str(int(Second))
            timeFont = Font.render(f"{Minute}:{secondText}",1, Black)
            screen.blit(timeFont, (985,20))
            

            pygame.display.flip()

    Clock.tick(60) # ensures a maximum of 60 frames per second

pygame.quit()