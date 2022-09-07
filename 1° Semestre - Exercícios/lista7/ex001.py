#Faça um programa em Python que leia uma matriz 2 x 3 de inteiros, imprima a matriz e a soma de todos os elementos.
from random import randint

a = [0]*2
soma = 0

for i in range(2):
    a[i] = [0]*3
    for j in range(3):
        a[i][j] = randint(1, 10)
        soma += a[i][j]

for i in range(2):
    print(*a[i])

print(f"Soma: {soma}")
