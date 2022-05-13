from random import randint

#print('Projeto de jogo de Batalha naval') 2 3 3 4 5

print('''
----Este é um jogo de Batalha Naval----
    
    Para jogar se escolhe as coordenadas em um grid 10x10
sendo essas coordenadas dadas por numeros de 1-10 e letras
A-J, dando um "tiro" na coordenada escolhida, caso acerte
sera definido como "fogo!", caso erre sera "agua!".

''')


def telaInicial():
    print('Deseja Jogar? Digite: \n1 - Sim\n2 - Não')
    resposta = input('Resposta: ')
    while resposta not in "12":
        resposta = input('Somente 1(sim) ou 2(não) como respostas validas:\n ')
    if resposta == "2": exit()


def telaJogador(gridJogador):
    print('--Escolha uma coordenada--')
    printGrid(gridJogador)




def geraGridAleatorio():
    grid = [[], [], [], [], [], [], [], [], [], []]
    for c in range(0, 10, 1):
        for d in range(0, 10, 1):
            grid[c].insert(d, randint(0, 3))
            if grid[c][d] != 0:
                grid[c][d] = 1
    return grid

def testeAcertoTiro(gridJogador, coordenadasTiro):
    acerto = True
    if gridJogador[coordenadasTiro[0]] [coordenadasTiro[1]] == 1: acerto = True
    else: acerto = False
    return acerto



def printGrid(grid):
    for c in range(0, 11, 1):
        print('\n')
        for d in range(0, 11, 1):
            print(grid[c][d], end='   ')

def convertLetraCoordenada(letra):
    numero = 0
    if letra == "a": numero = 0
    if letra == "b": numero = 1
    if letra == "c": numero = 2
    if letra == "d": numero = 3
    if letra == "e": numero = 4
    if letra == "f": numero = 5
    if letra == "g": numero = 6
    if letra == "h": numero = 7
    if letra == "i": numero = 8
    if letra == "j": numero = 9
    return numero


def digitarCoordenadasTiro():
    print('\nDigite a coordenada desejada (numero e letra): ')
    numero = input('Numero(1-10): ')
    while numero not in "12345678910" or int(numero) not in range(1, 11):
        print('Somente um numero valido(1-10): ')
        numero = input()
    letra = input('Letra(A-J): ').lower().strip()
    while letra.strip()[0] not in "abcdefghij" or len(letra) > 1:
        print('Somente uma letra valida(A-J): ')
        letra = input().lower().strip()
    numero = (int(numero) - 1)
    letra = convertLetraCoordenada(letra)
    coordenadasTiro = [numero, letra]
    return coordenadasTiro


gridJogador = [[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
              ['A', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['B', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['C', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['D', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['E', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['F', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['G', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['H', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['I', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
              ['J', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]


telaInicial()
gridAleatorio = geraGridAleatorio()


telaJogador(gridJogador)

coordenadaTiroJogador = digitarCoordenadasTiro()

if testeAcertoTiro(gridAleatorio, coordenadaTiroJogador) == True:
   print('Fogo!')
else:
    print('Agua!')










