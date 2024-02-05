import pygame
import time
from random import randint


def make_grid(grid_size, blank = True, cells = 0):
    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append('0')
        grid.append(row)

        #grid.append([row])
        #print(f'boobs{grid[0][0]}')
        #print(grid)




    if blank == True:
        return grid
    else:
        for i in range(cells):
            grid[randint(0, grid_size - 1)][randint(0, grid_size - 1)] = '1'
    return grid

def draw_map(map):# took this function from my alevel nea project, changed it so you can chaneg the grid size
    county = 0
    for each in map:
        countx = 0
        for i in each:
            match i:
                case '0':
                    pygame.draw.rect(screen, (255, 255, 255), [countx, county, 30, 30])
                case '1':
                    pygame.draw.rect(screen, (0, 0, 0), [countx, county, 30, 30])
            countx += 3
        county += 3


def next_evolution(grid):
    row_count = 0
    new_grid = make_grid(len(grid))
    for row in grid:
        cell_count = 0
        for cell in row:
            tally = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        pass
                    else:
                        try:
                            if grid[row_count + i][cell_count + j] == '1':
                                tally += 1
                        except:
                            # when it does the outer edges
                            pass

            if ((tally == 2 or tally == 3) and cell == '1') or \
                    (tally == 3 and cell == '0'):
                new_grid[row_count][cell_count] = '1'

            cell_count += 1

        row_count += 1

    return new_grid


if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()

    grid_size = int(input('enter size of grid: '))
    cells = int(input('enter the cells you want on the grid: '))
    grid = make_grid(grid_size, blank = False, cells = cells)
    '''grid = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '1', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ]'''

    screen = pygame.display.set_mode((grid_size*3, grid_size*3))
    pygame.display.set_caption = 'Game Of Life'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        draw_map(grid)
        pygame.display.flip()
        grid = next_evolution(grid)
        #clock.tick(1)



        pygame.display.flip()
