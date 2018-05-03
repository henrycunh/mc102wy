from math import sqrt

# Verifica se um número é primo
def isPrime(num):
    # Se o número for 2, é primo
    if num == 2:
        return 1
    # Se o número for dívisivel por 2, não é primo
    if not num % 2:
        return 0
    # Se não, começamos a comparar em 3, e vamos de dois em dois
    # até a raiz do número. Se ele não for divisível por nada
    # até sua própria raiz, não vai ser divisível por nada
    # depois dela.
    for i in range(3, round(sqrt(num)), 2):
        # Se o número for divisível por qualquer um desses, não é primo
        if not num % i:
            return 0
    # Se não for, é primo
    return 1
        

# Precisamos calcular os números primos mais próximos de N,
# antes e depois
n = int(input())
# Checamos se n é primo, com a função que fizemos, se for, ele é
# o primo mais próximo antes e depois
antes, depois = 0, 0
if isPrime(n):
    antes, depois = n, n
else:
    # Se não, devemos checar a partir de n até 2, qual o primo mais próximo antes dele
    # Partindo de n até 2 regressivamente
    for i in range(n, 1, -1):
        if isPrime(i):
            antes = i
            break
    # E então, partir de n até o primo mais próximo
    i = n + 1
    while 1:
        if isPrime(i):
            depois = i
            break
        i += 1
# Imprime o resultado
print("Maior primo menor ou igual a N: ", antes)
print("Menor primo maior ou igual a N: ", depois)