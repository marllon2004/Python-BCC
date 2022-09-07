#Elabore um programa em Python que gere uma matriz 4x6 e calcule e mostre a sua matriz transporta equivalente

from random import randint

a = [0]*4
b = [0]*6

for i in range(4):
    a[i] = [0]*6
    for j in range(6):
        a[i][j] = randint(1, 10)
    print(*a[i])

print()

for i in range(6):
    b[i] = [0]*4
    for j in range(4):
        b[i][j] = a[j][i]
    print(*b[i])