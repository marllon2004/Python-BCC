#Faça um programa em Python que gere uma matriz 10 x 10 de inteiros entre 1 e 50m imprima a matriz e o menor elemento de cada linha

from random import randint

a = [0]*10
b = []

for i in range(10):
    a[i] = [0]*10
    for j in range(10):
        a[i][j] = randint(1, 50)

for i in range(10):
    print(*a[i])

for i  in range(10):
    menor = a[i][0]
    for j in range(10):
        if a[i][j] <= menor:
            menor = a[i][j]
    b.append(menor)

print(f"\nMenores valores das linhas: {b}")