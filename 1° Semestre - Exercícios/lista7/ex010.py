#Escreva um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1 a 50, peça um número de uma linha qualquer, entre 0 e 9, e copie os elementos dessa linha para um vetor. Imprima a matriz e o vetor.

from random import randint

a = [0]*10
b = []


for i in range(10):
    a[i] = [0]*10
    for j in range(10):
        a[i][j] = randint(1, 50)
    print(*a[i])

n = int(input("Informe o número de uma linha [0 a 9]: "))

if n >= 0 and n <= 9:
    #print(f"\n{a[n]}")
    b = a[n]
    print(b)
else:
    print("Linha inexistente!")
