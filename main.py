import sys
import math
from settings import *
from material.grid import Grid
from material.sand import Sand
from material.stone import Stone
from material.water import Water

pygame.init()
window = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()

grid = Grid()
sand = []; stone = []; water = []; wood = []
hasStone = False; hasSand = True; hasWater = False; hasEraser = False; hasWood = False
grid.start_render()

run = True
while run:
    window.fill((55,55,55))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                hasSand = False; hasWater = False; hasStone = False; hasWood = False; hasEraser = True
            if event.key == pygame.K_1:
                hasSand = False; hasEraser = False; hasWater = False; hasWood = False; hasStone = True
            if event.key == pygame.K_2:			
                hasStone = False; hasEraser = False; hasWater = False; hasWood = False; hasSand = True
            if event.key == pygame.K_3:
                hasStone = False; hasEraser = False; hasSand = False; hasWood = False; hasWater = True
            if event.key == pygame.K_4:
                hasStone = False; hasEraser = False; hasSand = False; hasWater = False; hasWood = True
            if event.key == pygame.K_c:
                water.clear(); sand.clear(); stone.clear()
                grid.vals.clear(); grid.start_render()

    if pygame.mouse.get_pressed()[0]:
        mx,my = pygame.mouse.get_pos()
        if hasEraser: 
            for stn in stone[:]:
                if stn.x == (mx//size)*size and stn.y == (my//size)*size:
                    stone.remove(stn); grid.vals[((mx//size)*size,(my//size)*size)] = 0
        if grid.vals[(mx//size),(my//size)] == 0: 
            if hasStone: 
                    for i in range(math.ceil(PENCILSIZE/5)):
                        for j in range(math.ceil(PENCILSIZE/5)): 
                            stone += [Stone((((mx+i*size)-(0.5*PENCILSIZE))//size)*size,(((my+j*size)-(0.5*PENCILSIZE))//size)*size)]
            if hasSand: 
                for i in range(PENCILSIZE): sand += [Sand((((mx+i*size)-(0.5*PENCILSIZE*size))//size)*size,(my//size)*size)]
            if hasWater: 
                for i in range(PENCILSIZE): water += [Water((((mx+i*size)-(0.5*PENCILSIZE*size))//size)*size,(my//size)*size)]

    grid.draw()
    for stn in stone: stn.draw(window, grid)
    for snd in sand: snd.update(grid); snd.draw(window,grid)
    for wtr in water: wtr.update(grid); wtr.draw(window,grid)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
