from settings import *

class Water:
    def __init__(self,x=0,y=0):
        self.x = x; self.y = y
        self.color = (128,random.randint(197,230),222)
        self.id = 3

    def update(self, grid):
        self.check_down(grid)
        self.go_left_or_right(grid)

    def check_down(self, grid):
        current = (self.x//size, self.y//size)
        down = (self.x//size, (self.y+size)//size)
        try:
            if grid.vals[down] == 0:
                grid.vals[down] = self.id
                self.y += size
                grid.vals[current] = 0
        except: pass

    def go_left_or_right(self, grid):
        current = (self.x//size, self.y//size)
        left = ((self.x-size)//size, self.y//size)
        right = ((self.x+size)//size, self.y//size)
        down = (self.x//size,(self.y+size)//size)
        try:
            if grid.vals[down] == 1 or grid.vals[down] == 2 or grid.vals[down] == 3:
                r = random.randint(0,1)
                if grid.vals[left] == 0:
                    if r == 0: 
                        self.x -= size
                        grid.vals[left] = self.id 
                        grid.vals[current] = 0 
                if grid.vals[right] == 0:
                    if r == 1:
                        self.x += size
                        grid.vals[right] = self.id
                        grid.vals[current] = 0
        except: pass

    def draw(self, window, grid):
        current = (self.x//size, self.y//size)
        pygame.draw.rect(window, self.color, (self.x,self.y,size,size))
        grid.vals[current] = self.id