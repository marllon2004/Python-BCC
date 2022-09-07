#Faça um programa em Python que gere uma matriz 10 x 10 de inteiros entre 1 e 50, imprima a matriz e o menor elemento de cada coluna

from random import randint

a = [0]*10
b = []

for i in range(10):
    a[i] = [0]*10
    for j in range(10):
        a[i][j] = randint(1, 50)
    print(*a[i])

for i in range(10):
    menor = a[i][0]
    for j in range(10):
     if a[j][i] <= menor:
         menor = a[j][i]
    b.append(menor)

print(f"Menores valores das Colunas: {b}")