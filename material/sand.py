from settings import *

class Sand:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.color = (255,random.randint(200,255),12)
        self.id = 2

    def update(self, grid):
        self.check_down(grid)
        self.check_down_left(grid)
        self.check_down_right(grid)

    def check_down(self, grid):
        current = (self.x//size, self.y//size)
        down = (self.x//size,(self.y+size)//size)
        try:
            if grid.vals[down] == 0 or grid.vals[down] == 3: 
                grid.vals[down] = self.id
                self.y += size
                grid.vals[current] = 0
        except: pass

    def check_down_left(self, grid):
        current = (self.x//size, self.y//size)
        down = (self.x//size,(self.y+size)//size)
        down_left = ((self.x-size)//size, (self.y+size)//size)
        left = ((self.x-size)//size,self.y//size)
        try:
            if grid.vals[down] == self.id or grid.vals[down] == 1:
                if grid.vals[down_left] == 0 and grid.vals[left] == 0:
                    grid.vals[down_left] = self.id
                    self.x -= size; self.y += size
                    grid.vals[current] = 0
                if grid.vals[left] == 3 and grid.vals[down_left] == 3:
                    grid.vals[down_left] = self.id
                    self.x -= size; self.y += size
                    grid.vals[current] = 0
        except: pass

    def check_down_right(self, grid):
        current = (self.x//size, self.y//size)
        down = (self.x//size,(self.y+size)//size)
        down_right = ((self.x+size)//size, (self.y+size)//size)
        down_left = ((self.x-size)//size, (self.y+size)//size)
        right = ((self.x+size)//size,self.y//size)
        try:
            if (grid.vals[down] == self.id and grid.vals[down_left] == self.id) or (grid.vals[down] == 1 and grid.vals[down_left] == 1) or (grid.vals[down] == 3 and grid.vals[down_left] == 3):
                if (grid.vals[down_right] == 0 and grid.vals[right] == 0) or (grid.vals[down] == 3 and grid.vals[right] == 3):
                    grid.vals[down_right] = self.id
                    self.x += size; self.y += size
                    grid.vals[current] = 0
        except: pass

    def draw(self, window, grid):
        current = (self.x//size, self.y//size)
        pygame.draw.rect(window,self.color,(self.x,self.y,size,size))
        grid.vals[current] = self.id
        