## Lab 11
O exercício consiste de operações e validações em cima de uma estrutura de matriz. As noções que ele **tenta** transmitir são bem importantes no geral, e é importante que se entenda a sua resolução.

Abaixo está a demonstração passo a passo, com partes do código.

#### Entrada de dados
```python
rows, cols = (int(item) for item in input().split(" "))
```
Pegamos uma linha inteira de dados, e damos `split()` usando espaço como delimitador. Isso retorna um array, e então, usamos essa operação de iteração para aplicar a função `int()` em nos dois itens que serão gerados pelo `split()`, capturando os itens resultados em uma tupla.

Pegamos os dias usando 
```python 
days = int( input() )
```

Inicializamos uma lista, que será nossa matriz de contexto, pois irá armazenar outras listas, configurando assim umaa matriz.
```python
ctx = []
```

Iteramos pela quantidade de linhas `rows`, e damos inserimos no contexto, uma linha contendo todos os valores inseridos naquela linha, já transformados para int.

```python
for row in range(rows):
    ctx.append([int(item) for item in input().split(" ")])
```

#### Checagens e Iterações
Nesse estágio do algoritmo em que temos todos os dados que necessitamos, nos resta somente aplicar os filtros e fazer com essas informações as operações necessárias. Neste caso, precisamos percorrer cada elemento e estabelecer uma dentre cinco relações, sendo `x` o elemento atual:
- Se `x` for humano e existir um vizinho zumbi, x vira zumbi.
- Se `x` for zumbi e possuir dois vizinhos humanos, x é morto.
- Se `x` for zumbi e não possuir nenhum vizinho humano, x morre.
- Se `x` estiver vazio e tiver apenas 2 humanos vizinhos, x vira humano.
- Se não, `x` permanece como está.

Devemos então, iterar pela quantidade de dias **+1**, pois temos a **iteração 0** que é justamente a entrada que nois foi fornecida.
```python
for iteracao in range(days + 1):
```
Criamos uma nova lista que será o novo contexto, e copiamos cada linha do contexto atual para essa nova. Fazemos isso pois fazer uma cópia apenas da lista que chamamos de contexto seria uma **cópia rasa**, ou seja, as listas dentro da lista ainda estariam interligadas à variável. Fazemos uma cópia mais profunda da seguinte forma:
```python
# Lê-se como, para cada linha em contexto, crie uma cópia e adiciona à lista
new_ctx = [ row.copy() for row in ctx ]
```
Após isso, verificamos se a iteração não é a primeira
```python
if iteracao > 0:
```
E percorremos a matriz item a item, usando laços encadeados:
```python
# Linhas
for row in range(len(ctx)):
    # Colunas
    for col in range(len(ctx[row])):
```
O trecho `len(ctx[row])` pega a linha atual e retorna seu tamanho.

Armazenamos o item atual em `x = ctx[row][col]`, e o que vem a seguir é bastante importante.

#### Detecção de Humanos e Zumbis
No trecho:
```python
humans, zombies = detect(ctx, row, col)
```
Usamos essa função chamada detect, que recebe o contexto, a linha e a coluna atual, e supostamente retorna uma tupla contendo a quantidade de humanos e de zumbis. Mas como funciona a implementação dessa função?

Bom, primeiro a definimos com os parâmetros que necessitamos de forma a não alterar nenhuma informação original.
```python
def detect(ctx, row, col):
```
Em seguida, pegamos a quantidade de colunas e de linhas totais e definimos a lista que irá receber os vizinhos **válidos** e inicializamos as váriaveis que representam a quantidade de zumbis e humanos.
```python
rows, cols = ( len(ctx), len(ctx[0]) )
neigh = [] 
humans, zombies = 0, 0  
```
Note que o `0, 0` mesmo sem parêntese ainda é considerado uma tupla.

A seguir, temos que verificar uma série de condições para ver se podemos ou não acessar tal vizinho. Por exemplo, se o nosso X estiver no canto horizontal esquerdo, não podemos acessar um vizinho à sua esquerda, conforme ilustrado:

```python
  1    1   1
[ 1 ]  1   0
```
Nesse caso, temos que verificar para cada um dos cantos se é possível acessar os vizinhos. Existem formas muito mais elegantes de realizar essa checagem, optei por força bruta _(testar diretamente todos os casos)_ por questões de compreensão.

```python
# Verifica a linha acima
if row > 0: 
    neigh.append(ctx[row - 1][col]) 
    # Verifica coluna à esquerda
    if col > 0:  
        neigh.append(ctx[row - 1][col - 1])
    # Verifica coluna à direita
    if col < cols - 1: 
        neigh.append(ctx[row - 1][col + 1])
# Verifica a linha abaixo
if row < rows - 1: 
    neigh.append(ctx[row + 1][col])
    # Verifica coluna à esquerda
    if col > 0:
        neigh.append(ctx[row + 1][col - 1])
    # Verifica coluna à direita
    if col < cols - 1:
        neigh.append(ctx[row + 1][col + 1])
# Verifica coluna à esquerda na linha atual
if col > 0:
    neigh.append(ctx[row][col - 1])   
# Verifica coluna à direita na linha atual
if col < cols - 1:
    neigh.append(ctx[row][col + 1])
```

E então, com todos os vizinhos, verificamos quais são eles e adicionamos as váriaveis contador.
```python
for x in neigh: # Para cada vizinho
        if   x == 1: # Se for humano
            humans  += 1 
        elif x == 2: # Se for zumbi
            zombies += 1
```
E por fim, retornamos uma tupla com os valores.
```python
return (humans, zombies)
```
#### De volta à iteração
Possuindo a quantidade de humanos e zumbis, é fácil então lidar com as condições.
```python
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
```

E então, nos basta imprimir o novo contexto atual.
```python
# Printa a iteração atual
    print("iteracao %d" % iteracao)
    # Imprime todo elemento de toda linha, em ordem
    for row in new_ctx:
        for x in row:
            print(x, end="")
        # Quebra linha entres as linhas
        print()
```
E atribuir o novo contexto ao contexto atual.
```python
ctx = new_ctx
```