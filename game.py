import math
from engine import *
import pygame 
from pygame import gfxdraw
import random 

class ai():
	
	""" 
	Computer player. Picks fields at random. Not the brightest. 
	"""

	field = None
	def __init__(self, field):
		self.field = field

	def update(self):
		if self.field.is_ai_turn:
			possible = []
			for i, row in enumerate(self.field.board):
				for j, value in enumerate(row):	
					if value == 0: #free space
						possible.append((i,j))
			if len(possible) > 0:
				choosen_element = random.randrange(0,len(possible))		
				choice = possible[choosen_element]
				self.field.board[choice[0]][choice[1]] = self.field.current
				self.field.turns += 1
				self.field.flip_current()
				self.field.is_ai_turn = False

class field(render_item, mouse_listener):
	
	""" 
	Represents a field to play tictactoe in and handles the game logic. 
	"""

	current = 1
	is_ai_turn = False
	turns = 0
	ai = None
	won = False
	am = None
	X,O,WON = 0,0,0
	board = [
		[0,0,0],
		[0,0,0],	
		[0,0,0]
	]

	def __init__(self, surface, audio_manager_reference, audio_ids):
		self.surface = surface
		self.am = audio_manager_reference
		self.X = audio_ids[0]
		self.O = audio_ids[1]
		self.WON = audio_ids[2]
		self.ai = ai(self)
	
	def reset(self):
		self.board = [
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]	
		self.is_ai_turn = False
		self.current = 1
		self.turns = 0

	def draw_circle(self, x, y, radius, color):
		""" draw the circle on the board """
		gfxdraw.filled_circle(self.surface, x, y, radius, color)
		gfxdraw.filled_circle(self.surface, x, y, radius-10, (0,0,0))

	def draw_cross(self, x, y):
		pygame.draw.line(self.surface, (255,255,255), (((y-1)*150)+70,((x-1)*150)+70),(((y-1)*150)+190,((x-1)*150)+190),12)
		pygame.draw.line(self.surface, (255,255,255), ((((y-1)*150)+70),(((x-1)*150)+190)),  ((((y-1)*150)+190),(((x-1)*150)+70))    ,12)

	def draw(self):
		# draw the board
		for i in range(0,4):
			pygame.draw.rect(self.surface, (255,255,255), (50,50+i*150,450,10))
		for i in range(0,4):
			pygame.draw.rect(self.surface, (255,255,255), (50+i*150,50,10,460))
		# draw the pieces to the board
		x,y = 1,1
		for row in self.board:
			y=1
			for col in row:
				# pygame.draw.ellipse(self.surface, (255,255,255), (60,60,140,140), 6)
				if col == 2:
					self.draw_circle(y*130+20*(y-1),x*130+20*(x-1),75,(255,255,255))
				elif col == 1:
					self.draw_cross(x,y)
				y+=1
			x+=1
	
	def update(self):
		self.won = False
		self.ai.update()

		for row in self.board: #all rows
			if row[0] == row[1] and row[1] == row[2] and row[0] != 0:	
				self.won = True

		for i in range(0,2): #all cols
			if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
				self.won = True

		if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0: #diagonal one 
				self.won = True

		if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != 0: #diagonal two
				self.won = True
		if self.won:
			self.am.play(self.WON)
			self.reset()

		if self.turns == 9: # there is no further empty field available.
			self.reset()

	def flip_current(self):
		
		""" 
		This function flips the variable 'current' to keep track of 
		which side is making a move now 
		"""

		self.current = (self.current+1)%3
		if self.current == 0: 		
			self.current = 1
		
	def mouse_click(self, e):
		x,y = e[0], e[1]
		if x > 60 and x <= 500:
			if y > 60 and y <= 500: # it is inside the gaming area.
				x,y = x-60, y-60
				i,j = math.trunc(x/160), math.trunc(y/160)

				if self.board[j][i] != 0:
					return # this was not an empty field so ignore the user input.

				self.board[j][i] = self.current

				if self.current == 1:
					self.am.play(self.X)

				else: 
					self.am.play(self.O)
				
				self.turns += 1
				self.flip_current()
				self.is_ai_turn = not self.is_ai_turn
