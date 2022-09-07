#Elabore um programa em Python que gere uma matriz 5x5 e calcule e mostre a diagonal principal e a secundária

from random import randint

a = [0]*5
diagonalP = []
diagonalS = []

for i in range(5):
    a[i] = [0]*5
    for j in range(5):
        a[i][j] = randint(1, 10)

    print(*a[i])

for i in range(5):
    diagonalS.append(a[i][j - i])
    for j in range(5):
        if i == j:
            diagonalP.append(a[i][j])

print(f"\nDiagonal Principal: {diagonalP}"
      f"\nDiagonal Secundaria: {diagonalS}")
