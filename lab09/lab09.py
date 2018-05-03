# -*- coding: utf-8 -*-

# A resolução do problema consiste em pegar todas as
# possibilidades de lucro, e seguindo algumas restrições,
# apresentar as compras de pacote que geram o maior lucro.
#
# As restrições são: 
# Somente um pacote pode ser comprado por dia
# Somente um pacote pode ser comprado por empresa

# Número de dias
n = int(input())
# Lista de pacotes
pacotes = []

# Lê todas as ações e gera os pacotes que podem render algum lucro
for empresa in range(4):
    acoes = [] # Lista de ações
    for dia in range(n):
        acao = { "valor" : float(input()), "empresa" : empresa, "dia" : dia  }
        for dia_compra in range(dia):
            lucro = acao['valor'] - acoes[dia_compra]['valor'] 
            if lucro > 0:
                pacotes.append({
                    "lucro"     : lucro,
                    "empresa"   : empresa,
                    "dia_compra": dia_compra,
                    "dia_venda" : dia
                })
        acoes.append(acao)

pacotes_selecionados = []
# Com todos os pacotes, podemos então continuar a verificar os requisitos
for empresa in range(4):
    # Pega todos os pacotes da empresa
    pacotes_empresa = [pacote for pacote in pacotes if pacote['empresa'] == empresa]
    maior_pacote = { "lucro" : -1 }
    for pacote in pacotes_empresa:
        if pacote['lucro'] > maior_pacote['lucro']:
            # Devemos checar se não existe um outro pacote no dia que tem valor maior
            pacotes_no_dia = [p for p in pacotes if p['dia_compra'] == pacote['dia_compra']]
            # Se não existir pacote no dia, então ele é maior do dia
            if pacotes_no_dia:
                # Pegamos o maior pacote desse dia, mas ele deve ser o maior da empresa selecionada
                maior_pacote_no_dia = { "lucro" : -1 }
                for pacote_dia in pacotes_no_dia:
                    if pacote_dia['lucro'] > maior_pacote_no_dia['lucro']:
                        pacotes_da_empresa = [p for p in pacotes if p['empresa'] == pacote_dia['empresa']]
                        maior_pacote_empresa = max(pacotes_da_empresa, key = lambda p: p['lucro'])
                        if maior_pacote_empresa['lucro'] <= pacote_dia['lucro']:
                            maior_pacote_no_dia = pacote_dia    

                # Se o pacote ainda for maior, adicionamos como maior pacote
                if pacote['lucro'] >= maior_pacote_no_dia['lucro']:
                    maior_pacote = pacote 
            else:
                maior_pacote = pacote
    pacotes_selecionados.append(maior_pacote)

# Com isso, temos todos os pacotes, só falta exibi-los
# Antes, pegamos todos os pacotes que não tem lucro como -1 (os que realmente existem)
pacotes_selecionados = [pacote for pacote in pacotes_selecionados if pacote['lucro'] > 0]
# Verificamos se existe algum pacote, se não, o lucro é 0
if pacotes_selecionados:
    # Inicializa acumulador total de lucro
    lucro_total = 0
    # Se existem, percorremos pelos pacotes e imprimimos suas informações
    for pacote in pacotes_selecionados:
        print("acao %d: compra %d, venda %d, lucro %.2f" % (pacote['empresa'] + 1, pacote['dia_compra'] + 1, pacote['dia_venda'] + 1, pacote['lucro']))
        lucro_total += pacote['lucro']
    # Calcular e exibir total de lucro
    print("Lucro: %.2f" % lucro_total)
else:
    print("Lucro: %.2f" % 0)