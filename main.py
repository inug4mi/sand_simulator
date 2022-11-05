import sys
from settings import *
from material.grid import Grid
from material.sand import Sand
from material.stone import Stone
from material.water import Water

pygame.init()
window = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()

grid = Grid()
sand = []; stone = []; water = []
hasStone = False; hasSand = True; hasWater = False; hasEraser = False

run = True
while run:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                hasSand = False; hasWater = False; hasStone = False; hasEraser = True;
            if event.key == pygame.K_1:
                hasSand = False; hasEraser = False; hasWater = False; hasStone = True
            if event.key == pygame.K_2:			
                hasStone = False; hasEraser = False; hasWater = False; hasSand = True
            if event.key == pygame.K_3:
                hasStone = False; hasEraser = False; hasSand = False; hasWater = True
            if event.key == pygame.K_c:
                water.clear(); sand.clear(); stone.clear()

    if pygame.mouse.get_pressed()[0]:
        mx,my = pygame.mouse.get_pos()
        if hasEraser: 
            for stn in stone[:]:
                if stn.x == (mx//size)*size and stn.y == (my//size)*size:
                    stone.remove(stn); grid.vals[((mx//size)*size,(my//size)*size)] = 0
        if grid.vals[(mx//size),(my//size)] == 0:
            if hasStone: stone += [Stone((mx//size)*size,(my//size)*size)]
            if hasSand: sand += [Sand((mx//size)*size,(my//size)*size)]
            if hasWater: water += [Water((mx//size)*size,(my//size)*size)]

    grid.draw()
    for stn in stone: stn.draw(window, grid)
    for snd in sand: snd.update(grid); snd.draw(window,grid)
    for wtr in water: wtr.update(grid); wtr.draw(window,grid)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()