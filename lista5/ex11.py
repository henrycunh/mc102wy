def verifica(mat):
    resposta = [[] for x in range(len(mat))]
    for i in range(len(mat)):
        # Para verficar se tem entrada, precisamos checar
        # se na coluna i, existe algum 1
        print([mat[j][i] for j in range(len(mat))])
        resposta[i].append(
            1 in [mat[j][i] for j in range(len(mat))]
        )
        # Para verificar se tem saída, só checar se
        # na linha i existe algum 1
        print(mat[i])
        resposta[i].append(
            1 in mat[i]
        )
        print()
        # Para verificar se está isolada, só checar se
        # não inserimos 1 nas respostas até então
        resposta[i].append(
            1 not in resposta[i]
        )
    return resposta
