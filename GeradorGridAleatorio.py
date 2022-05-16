from random import randint

def geraGridAleatorio():
    grid = [[], [], [], [], [], [], [], [], [], []]
    for c in range(0, 10, 1):
        for d in range(0, 10, 1):
            grid[c].insert(d, randint(0, 2))
            if grid[c][d] != 0:
                grid[c][d] = 1
    for c in range(1, 9, 1):
        for d in range(1, 9, 1):
            if grid[c][d] == 0 and grid[c+1][d] != 0 and grid[c-1][d] != 0 \
                                and grid[c][d+1] != 0 and grid[c][d-1] != 0:
                grid[c][d] = 1
    return grid

def printGrid(grid):
    for c in range(0, 10, 1):
        print('\n')
        for d in range(0, 10, 1):
            print(grid[c][d], end='   ')

gridAleatorio = geraGridAleatorio()
printGrid(gridAleatorio)

