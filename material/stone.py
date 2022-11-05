from settings import *

class Stone:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
		self.color = (130,random.randint(125,150),150)# (r,g,b)
		self.id = 1

	def draw(self, window, grid):
		pygame.draw.rect(window,self.color,(self.x//size*size,self.y//size*size,size,size))
		grid.vals[(self.x//size,self.y//size)] = self.id