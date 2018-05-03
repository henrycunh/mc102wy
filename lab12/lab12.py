#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome:
# RA:

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

############ Funcao: atualiza_posicao
#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco (positivo para direita, negativo para a esquerda) 
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario 
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#
def atualiza_posicao(l, a, x, desl, rot):
    nL, nA, nX = 0, 0, 0
    # Implementar a funcao e trocar o valor de retorno
    if rot == 1: #caso haja rotacao, troca-se a altura e a largura do bloco uma pela outra
        l, a = nA, nL
    if x + desl < 0: # bloco bate na parede a esquerda
         nX = 0 # posicao do bloco deve ficar junto a parede
    elif x + l + desl > LARGURA_TABULEIRO - 1: # (x + l) nos da a posicao da quina direita do bloco; neste caso, o bloco bate na parede a direita
            nX = LARGURA_TABULEIRO - l # posicao do bloco deve ficar junto a parede
    else: # caso o bloco nao bata em nenhuma parede
        nX = x + desl

    return nL, nA, nX 

# Funcao: encontra_y
#
# Parametros:
#    mat: matriz representando o tabuleiro 
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#
def encontra_y(mat, l, x):
    y = ALTURA_TABULEIRO - 1
    encontrou = False
    while not encontrou: # Itera as linhas
        
    return y

######### Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro, ou 0 caso contrario.
#
def posicao_final_valida(a, y):
    # Implementar a funcao e trocar o valor de retorno
    if a + y > ALTURA_TABULEIRO - 1: # se o bloco cair e ficar para fora do tabuleiro, o jogo acaba
        return 0
    else: # caso contrario, ele continua
        return 1

# Funcoes: posiciona_bloco
#
# Parametros:
#    mat: matriz do tabuleiro 
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posições ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#
def posiciona_bloco(mat, l, a, x, y):
    # Implementar a funcao
    for i in range(a):
        for j in range(a):
            mat[y - i][j + a] = 1
            
    return None

# Funcoes: atualiza_matriz
# 
#    mat: matriz do tabuleiro 
#
#         Deve remover as linhas totalmente preenchidas do tabuleiro copiando
#         linhas posicionadas acima.
# Retorno:
#   retorna o numero de linhas totalmente preenchidas que foram removidas apos
#   a atualizacao do tabuleiro.
#
def atualiza_matriz(mat):
    # Implementar a funcao e trocar o valor de retorno
    linhas_removidas = 0
    descer = 0
    for i in range(ALTURA_TABULEIRO-1, -1, -1): # itera as linhas de cima para baixo
        for j in range(LARGURA_TABULEIRO): # itera as colunas
            if mat[i][j] == 1: # se o espaco estiver preenchido:
                descer = descer + 1 # adiciona-se 1 na variavel contadora descer
        if descer == LARGURA_TABULEIRO: # se descer for igual a largura do tabuleiro, significa que todos os espacos da linha estao preenchidos e ela deve ser removida
            linhas_removidas = linhas_removidas + 1
            for li in range(i, ALTURA_TABULEIRO): # itera as linhas a partir da linha que foi removida
                for c in range(LARGURA_TABULEIRO): # itera as colunas
                    mat[li][c] = mat[li+1][c]

    return linhas_removidas




     

