from random import randint

#print('Projeto de jogo de Batalha naval') 2 3 3 4 5

print('''
----Este é um jogo de Batalha Naval----
    
    Para jogar se escolhe as coordenadas em um grid 10x10
sendo essas coordenadas dadas por numeros de 1-10 e letras
A-J, dando um "tiro" na coordenada escolhida, caso acerte
sera definido como "fogo!", caso erre sera "agua!", deseja
jogar?

Digite: 1 - Sim
        2 - Não''')


def gridAleatorio():
    grid = [[], [], [], [], [], [], [], [], [], []]
    for c in range(0, 10, 1):
        for d in range(0, 10, 1):
            grid[c].insert(d, randint(0, 1))
    return grid

def printGrid(grid):
    for c in range(0, 10, 1):
        print(grid[c])

grids = gridAleatorio()
printGrid(grids)




