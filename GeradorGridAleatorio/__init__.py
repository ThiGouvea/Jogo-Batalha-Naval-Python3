from random import randint


def Gera_Grid_Aleatorio():
    corvete = [1, 4, 2]
    submarino = [2, 3, 3]
    fragata = [3, 2, 4]  # [numero da nave, quantidade, tamanho]
    destruidor = [4, 2, 5]
    cruzador = [5, 1, 6]
    posicoes = []
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

    grid = Testar_E_Colocar_Nave_Grid(grid, cruzador[2], cruzador[1], cruzador[0])
    grid = Testar_E_Colocar_Nave_Grid(grid, fragata[2], fragata[1], fragata[0])
    grid = Testar_E_Colocar_Nave_Grid(grid, corvete[2], corvete[1], corvete[0])
    grid = Testar_E_Colocar_Nave_Grid(grid, submarino[2], submarino[1], submarino[0])
    grid = Testar_E_Colocar_Nave_Grid(grid, destruidor[2], destruidor[1], destruidor[0])
    return grid

def Testar_E_Colocar_Nave_Grid(grid, tamanhoNave, quantidadeNave, numeroNave):
    novoGrid = grid
    quantidadeIteracoes = quantidadeNave
    while quantidadeIteracoes != 0:
        lugarAleatorio = [randint(0, 9), randint(0, 9)]
        posicoes = Testar_Posicao_Vazia(novoGrid, lugarAleatorio[0], lugarAleatorio[1], tamanhoNave)
        if novoGrid[lugarAleatorio[0]][lugarAleatorio[1]] == 0 and posicoes[4]:
            novoGrid = Colocar_Nave_Grid(novoGrid, lugarAleatorio[0], lugarAleatorio[1], tamanhoNave, posicoes, numeroNave)
            quantidadeIteracoes -= 1
    return novoGrid

def Colocar_Nave_Grid(grid, posicaoX, posicaoY, tamanhoNave, posicoesValidas, numeroNave):
    novoGrid = grid
    orientacaoAleatoria = randint(0, 3)
    while not posicoesValidas[orientacaoAleatoria]:
        orientacaoAleatoria = randint(0, 3)


    if orientacaoAleatoria == 0:
        for i in range(0, tamanhoNave, 1):
            novoGrid[posicaoX - i][posicaoY] = numeroNave
        return novoGrid
    elif orientacaoAleatoria == 1:
        for i in range(0, tamanhoNave, 1):
            novoGrid[posicaoX + i][posicaoY] = numeroNave
        return novoGrid
    elif orientacaoAleatoria == 2:
        for i in range(0, tamanhoNave, 1):
            novoGrid[posicaoX][posicaoY - i] = numeroNave
        return novoGrid
    elif orientacaoAleatoria == 3:
        for i in range(0, tamanhoNave, 1):
            novoGrid[posicaoX][posicaoY + i] = numeroNave
        return novoGrid


def Testar_Posicao_Vazia(grid, posicaoX, posicaoY, tamanhoNave):
    cima = True
    baixo = True
    frente = True
    atras = True
    possuiVazio = True

    for i in range(0, tamanhoNave, 1):

        if posicaoX - i < 0:
            cima = False
        elif grid[posicaoX - i][posicaoY] != 0:
            cima = False
        if posicaoX + i > 9:
            baixo = False
        elif grid[posicaoX + i][posicaoY] != 0:
            baixo = False
        if posicaoY - i < 0:
            frente = False
        elif grid[posicaoX][posicaoY - i] != 0:
            frente = False
        if posicaoY + i > 9:
            atras = False
        elif grid[posicaoX][posicaoY + i] != 0:
            atras = False

    if not cima and not baixo and not frente and not atras:
        possuiVazio = False

    print(cima, baixo, frente, atras, possuiVazio)
    return [cima, baixo, frente, atras, possuiVazio]



def Print_Grid(gridCheio):
    for c in range(0, 10, 1):
        print('\n')
        for d in range(0, 10, 1):
            print(gridCheio[c][d], end='   ')


