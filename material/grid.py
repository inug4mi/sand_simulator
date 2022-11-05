from settings import *
class Grid:
	def __init__(self):
		self.width = W
		self.height = H
		self.id = 0
		self.vals = {}

	def draw(self):
		for x in range(self.width//size):
			for y in range(self.height//size):
				self.vals.update({(x,y):self.id})
				#pygame.draw.rect(window,(225,225,225),(size*x,y*size,size,size),1)

