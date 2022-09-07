# Elabore um programa em Python que gere uma matriz aleatória (9x9), com números entre 0 e 10, imprima-a. Após, peça o quadrante desejado e imprima os elementos desse quadrante.

from random import randint

a = [0]*9
q1 = [0]*4
q2 = [0]*4
q3 = [0]*4
q4 = [0]*4

for i in range(9):
    a[i] = [0]*9
    for j in range(9):
        a[i][j] = randint(1, 50)
    print(*a[i])

q = int(input("\nInforme o número do quadrante: \n"))

if q > 4 or q < 0:
    print("Quadrante inexistente!")

for i in range(4):
    q1[i] = [0]*4
    q2[i] = [0]*4
    q3[i] = [0]*4
    q4[i] = [0]*4
    for j in range(4):
        q1[i][j] = a[i][j]
        q2[i][j] = a[i][j+5]
        q3[i][j] = a[i+5][j]
        q4[i][j] = a[i+5][j+5]

    if q == 1:
        print(q1[i])
    elif q == 2:
        print(q2[i])
    elif q == 3:
        print(q3[i])
    elif q == 4:
        print(q4[i])