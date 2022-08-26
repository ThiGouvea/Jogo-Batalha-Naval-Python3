from random import randint


def Gera_Grid_Aleatorio():
    corvete = [0, 4, 2]
    submarino = [1, 3, 3]
    fragata = [2, 2, 4]  # [numero da nave, quantidade, tamanho]
    destruidor = [3, 2, 5]
    cruzador = [4, 1, 6]
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(0, corvete[1], 1):
        lugarAleatorio = [randint(0, 9), randint(0, 9)]
        posicoesValidas = Testar_Posicao_Vazia(grid, lugarAleatorio[0], lugarAleatorio[1], corvete[2])
        grid = Colocar_Nave_Grid(grid, lugarAleatorio[0], lugarAleatorio[1], corvete[2], posicoesValidas)

    return grid


def Colocar_Nave_Grid(grid, posicaoX, posicaoY, tamanhoNave, posicoesValidas):
    novoGrid = grid
    if posicoesValidas[0]:
        for i in range(0, tamanhoNave, 1):
            novoGrid[posicaoX - i][posicaoY] = 1


def Testar_Posicao_Vazia(grid, posicaoX, posicaoY, tamanhoNave):
    cima = True
    baixo = True
    frente = True
    atras = True

    for i in range(0, tamanhoNave, 1):
        if grid[posicaoX - i][posicaoY] == 1:
            cima = False
        elif grid[posicaoX + i][posicaoY] == 1:
            baixo = False
        elif grid[posicaoX][posicaoY + i] == 1:
            frente = False
        elif grid[posicaoX][posicaoY - i] == 1:
            atras = False

    return [cima, baixo, frente, atras]


def Print_Grid(gridCheio):
    for c in range(0, 10, 1):
        print('\n')
        for d in range(0, 10, 1):
            print(gridCheio[c][d], end='   ')


gridAleatorio = Gera_Grid_Aleatorio()

Print_Grid(gridAleatorio)

