import pygame
import random
from engine import *
from game import *

# pygame constants
width = 560
height = 560
fps = 60

# pygame initialization
pygame.init()
pygame.mixer.init() 
screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

pygame.display.set_caption("TicTacToe")

pool = render_pool()
am = audio_manager()
X = am.add("x.wav")
O = am.add("o.wav")
WON = am.add("won.wav")

def init():
	pool.add(field(screen, am, [X,O,WON]))

init()
## Game loop
running = True
while running:

	clock.tick(fps)	

	for event in pygame.event.get(): # event handling
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pool.mouse_down(event.pos[0],event.pos[1])

	screen.fill((0,0,0))

	pool.render_and_update() # update all elements of the game

	pygame.display.flip()	   

pygame.quit()
