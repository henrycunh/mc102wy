# Função de aproximação
def aprox(numero, n):
    if n == 1:
        return numero / 2
    else:
        x = aprox(numero, n - 1)
        return  x - ((x * x - numero) / (2 * x))
print(aprox(int(input()), 20))