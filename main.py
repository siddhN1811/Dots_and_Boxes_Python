#removing welcome message
from os import *
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

import pygame
#This is used to initialise all of the pygame modules. Without this the modules would not work
pygame.init()  
#INITIALIZATION OF VARIABLES
WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('CONNECT DOTS')

white = (255,255,255)
blue = (0,0,255)
black =(0,0,0)

running = True
pos = None
#for modular grid
x = int(input("Enter No. of rows: "))
y = int(input("Enter No. of columns: "))


while running:
    win.fill(white)
    
    all_events =pygame.event.get()
    #bg grid
    for i in range(100):
        for j in range(100):
            # parameters/arguments whatever -> where, colour, position(x,y) , radius
            pygame.draw.circle(win, '#EDEDED', (j*10 , i*10 ), 1)

    for event in all_events :  
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:  #getting the position of the mouse when the mouse button is pressed
            pos = pygame.mouse.get_pos()


    for i in range(x):
        for j in range(y):
             # parameters/arguments whatever -> where, colour, position(x,y) , radius
             pygame.draw.circle(win , blue, (j*40 +60, i*40 + 60), 5 )



    if pos:
        #drawing the circle in that positon when the mouse button is clicked 
        pygame.draw.circle(win , black , pos , 3 )


    pygame.display.update() #updates the win

pygame.quit()

print("gg") #time pass gg