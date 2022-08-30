from random import randint
import GeradorGridAleatorio



gridOculto = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]           #0 = não revelado, 6 agua, 1-5 naves

def Fazer_Uma_Jogada(gridOculto):
    contagemTotal = 0
    jogadaFeita = [0, 0]
    posicaoVazia = []
    for x in range(0, 10, 1):
        for y in range(0, 10, 1):
            contagemTotal += gridOculto[x][y]

    if contagemTotal == 0:
        jogadaFeita = [randint(0, 9), randint(0, 9)]

    else:
        for x in range(0, 10, 1):
            for y in range(0, 10, 1):
                if gridOculto[x][y] == 1:
                    posicaoVazia = GeradorGridAleatorio.Testar_Posicao_Vazia(gridOculto, x, y, 1)
                    if posicaoVazia[4]:




    return jogadaFeita

def Testar_Acerto(gridRevelado, coordenadaX, coordenadaY):
    if gridRevelado[coordenadaX][coordenadaY] > 0: return True
    else: return False

def Definir_Local_Jogada(posicoesVazia, coordenadaX, coordenadaY):

