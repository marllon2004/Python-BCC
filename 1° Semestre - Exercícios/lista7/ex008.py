#Elabore um programa em Python que leia duas matrizes A (mxn) e B (pxq) e calcule e mostre a matriz Python que é a soma de A com B (caso a soma seja possível).

from random import randint

m = int(input("Informe a quantidade de linhas do Vetor A: "))
n = int(input("Informe a quantidade de colunas do Vetor A: "))

p = int(input("Informe a quantidade de linhas do Vetor B: "))
q = int(input("Informe a quantidade de colunas do Vetor B: "))

a = [0]*m
b = [0]*p
c = [0]*m

for i in range(m):
    a[i] = [0]*n
    c[i] = [0]*n
    for j in range(n):
        a[i][j] = randint(1, 50)
    print(*a[i])

print()

for i in range(p):
    b[i] = [0]*q
    for j in range(q):
        b[i][j] = randint(1, 50)
    print(*b[i])

print()

if m == p and n == q:
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
        print(*c[i])
else:
    print("\nDimensões entre vetores distintas!"
          "\nNão é possível somar os valores!")