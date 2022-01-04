from abc import ABC, abstractmethod

# This is the baseclass of every render item.
class render_item(ABC):
	pool = None

	@abstractmethod
	def draw(self):
		None

	@abstractmethod
	def update(self):
		None

	def pool(self,pool):
		self.pool = pool
		
class render_pool():
	elements = []

	def add(self,element):
		assert isinstance(element, render_item)
		element.pool(self)
		self.elements.append(element)

	def remove(self,id_element):
		None
	
	def render(self):
		for element in self.elements:
			element.draw() 

	def update(self):
		for element in self.elements:
			element.update() 
	
	def render_and_update(self):
		for element in self.elements:
			element.update() 
			element.draw()
		
class dot_item(render_item):
	def draw(self):
		print("I am rendering")
	def update(self):
		None
