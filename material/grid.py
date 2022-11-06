from settings import *
class Grid:
	def __init__(self):
		self.width = W
		self.height = H
		self.id = 0
		self.vals = {}

	def start_render(self):
		for x in range(self.width//size):
			for y in range(self.height//size):
				self.vals.update({(x,y):self.id})

	def draw(self):
		for x in range(self.width//size):
			for y in range(self.height//size):
				self.vals.update({(x,y):self.id})

