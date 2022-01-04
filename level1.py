from abc import ABC

# This is the baseclass of every render item.
class render_item(ABC):
	def draw(self):
		None
	def update(self):
		None

class render_pool():
	def add(element):
		assert isinstance( element,render_item)
		None
