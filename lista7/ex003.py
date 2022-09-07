#Faça um programa em Pythoon que gere uma matriz 10 x 10 de inteiros aleatórios entre 1 e 50, imprima a matriz e a soma de todos os elementos de cada linha

from random import randint

a = [0]*10
b = []

for i in range(10):
    a[i] = [0]*10
    soma = 0
    for j in range(10):
        a[i][j] = randint(1, 50)
        soma += a[i][j]
    b.append(soma)

for i in range(10):
    print(*a[i])

print(f"\nSoma das linhas: {b}")