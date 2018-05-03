# Entrada de dados
n = int(input())
numeros = []
for i in range(n):
    numeros.append(float(input()))
# Saída de dados
print("Intervalo [0..25]: ", len([x for x in numeros if x >= 0 and x <= 25]))
print("Intervalo [26..50]: ", len([x for x in numeros if x >= 26 and x <= 50]))
print("Intervalo [51..75]: ", len([x for x in numeros if x >= 51 and x <= 75]))
print("Intervalo [76..100]: ", len([x for x in numeros if x >= 76 and x <= 100]))