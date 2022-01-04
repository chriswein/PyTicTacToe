from engine import *
import pygame 

class field(render_item):
	def __init__(self, surface):
		self.surface = surface
	def draw(self):
		# draw the board
		for i in range(0,4):
			pygame.draw.rect(self.surface, (255,255,255), (50,50+i*150,450,10))
		for i in range(0,4):
			pygame.draw.rect(self.surface, (255,255,255), (50+i*150,50,10,460))
		# draw the pieces
		None
	
	def update(self):
		None
