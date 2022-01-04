import pygame
import random
from engine import *
from game import *


WIDTH = 560
HEIGHT = 560
FPS = 60

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()     ## For syncing the FPS
pool = render_pool()

## init game elements
def init():
	pool.add(field(screen))
	None

init()
## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False


    #2 Update


    #3 Draw/render
    screen.fill(BLACK)
    pool.render_and_update()

    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
