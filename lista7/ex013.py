#Escreva um programa em Python que gere uma matriz M[5][5], com números aleatórios entre 1 e 50. Imprima a matriz. A seguir, troque os elementos da diagonal princiapl com os elementos da diagonal decondária. IMprima a nova matriz

from random import randint

a = [0]*5
dP = []
dS = []

for i in range(5):
    a[i] = [0]*5
    for j in range(5):
        a[i][j] = randint(1, 50)
        if i == j:
            dP.append(a[i][j])
    print(*a[i])

print()

for i in range(5):
    dS.append(a[i][j-i])
    for j in range(5):
        if i == j:
            a[i][j] = dS[j]
    a[i][j-i] = dP[i]
    print(*a[i])
