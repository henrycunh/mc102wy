n = int(input())
pot = 0
numero_final = 0
while n > 0:
    if n % 2:
        numero_final += 10**pot
    pot += 1
    n = n // 2
print(numero_final)
    