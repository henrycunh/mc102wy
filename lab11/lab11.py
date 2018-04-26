# -*- coding: utf-8 -*-

# Função que diz quantos humanos e zumbis existem ao redor do
# ponto na matriz
def detect(ctx, row, col):
    # Pegando a quantidade de linhas e colunas da matriz
    rows, cols = (len(ctx), len(ctx[0]))
    neigh = [] # Vizinhos válidos
    humans, zombies = (0, 0) # Inicializa as duas variaveis como 0

    # Fazemos verificação por força bruta
    if row > 0: # Verifica se não está na primeira linha
        neigh.append(ctx[row - 1][col]) # Adiciona o vizinho diretamente acima
        if col > 0: # Verifica se não está na primeira coluna 
            neigh.append(ctx[row - 1][col - 1])
        if col < cols - 1: # Verifica se não está na última coluna
            neigh.append(ctx[row - 1][col + 1])
    if row < rows - 1: # Verifica se não está na última linha
        neigh.append(ctx[row + 1][col])
        if col > 0:
            neigh.append(ctx[row + 1][col - 1])
        if col < cols - 1:
            neigh.append(ctx[row + 1][col + 1])
    if col > 0:
        neigh.append(ctx[row][col - 1])            
    if col < cols - 1:
        neigh.append(ctx[row][col + 1])            
    
    for x in neigh: # Para cada vizinho
        if   x == 1: # Se for humano
            humans  += 1 
        elif x == 2: # Se for zumbi
            zombies += 1
    return (humans, zombies) # Retorna uma tupla contendo a quantidade de humanos e de zumbis

# Recebendo as linhas e colunas da matriz (através de uma propagação em tupla)
rows, cols = (int(item) for item in input().split(" "))
# Dias de iteração
days = int(input())

# Matriz contexto
ctx = []

# Itera pelas linhas adicionando-as na matriz
for row in range(rows):
    # Adiciona a lista de valores na lista de listas (matriz)
    ctx.append([int(item) for item in input().split(" ")])

for iteracao in range(days + 1):
    # Irá armazenar uma cópia do contexto
    new_ctx = [ row.copy() for row in ctx ]

    if iteracao > 0:
        # Realiza a iteração verdadeira e calcula as relações item a item
        for row in range(len(ctx)):
            for col in range(len(ctx[row])):
                # Temos 5 relações possíveis, que dependem da vizinhança do item:
                #   *> se x for humano e existir um vizinho zumbi, x vira zumbi
                #   *> se x for zumbi e possuir dois vizinhos humanos, x é morto
                #   *> se x for zumbi e não possuir nenhum vizinho humano, x morre
                #   *> se x estiver vazio e tiver apenas 2 humanos vizinhos, x vira humano
                #   *> se não, x permanece como está
                # Devemos então testar para cada um dos casos e fazer a alteração
                x = ctx[row][col]
                # Pega a quantidade de vizinhos zumbis e humanos
                humans, zombies = detect(ctx, row, col)
                # print(x, humans, zombies, end=" ")
                # Checa se x é humano 
                if(x == 1):
                    # Se tiver mais de um zumbi, transforma zumbi
                    new_ctx[row][col] = 2 if zombies > 0 else 1
                # Checa se x é zumbi
                elif(x == 2):
                    # Se não tiver exatamente um zumbi, morre (morto ou por fome)
                    new_ctx[row][col] = 0 if humans != 1 else 2
                # Checa se tá vazio
                else:
                    # Se tiver exatamente dois humanos, gera um novo
                    new_ctx[row][col] = 1 if humans == 2 else 0
    # Printa a iteração atual
    print("iteracao %d" % iteracao)
    # Imprime todo elemento de toda linha, em ordem
    for row in new_ctx:
        for x in row:
            print(x, end="")
        # Quebra linha entres as linhas
        print()
    # Atribue o novo contexto ao contexto atual    
    ctx = new_ctx
    
    