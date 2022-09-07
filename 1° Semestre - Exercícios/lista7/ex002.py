#Faça um programa em Python que gere uma matriz 10 x 10 de inteiros aleatórios entre 1 e 50, imprima a matriz e a média de todos os elementos
from random import randint

a = [0]*10
media = 0

for i in range(10):
    a[i] = [0]*10
    for j in range(10):
        a[i][j] = randint(1, 50)
        media += a[i][j]

for i in range(10):
    print(*a[i])

print(f"Media: {media / (len(a)*10)}")