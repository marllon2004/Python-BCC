#Faça um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1 a 50 e copie para um vetor de 10 elementos, os números da diagonal principal. Imprima a matriz e o vetor.

from random import randint

a = [0]*10
d = []

for i in range(10):
    a[i] = [0]*10
    for j in range(10):
        a[i][j] = randint(1, 50)
    print(*a[i])

for i in range(10):
    for j in range(10):
        if i == j:
            d.append(a[i][j])
print(f"\n{d}")