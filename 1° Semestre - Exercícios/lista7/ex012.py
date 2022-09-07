#Faça um programa em Python que gere uma matriz 5x5 com valores entre 1 e 50. Imprima a matriz e troque uma linha por outra linha informada pelo usuário. Mostre a matriz após a troca.

from random import randint

a = [0]*5

for i in range(5):
    a[i] = [0]*5

    for j in range(5):
        a[i][j] = randint(1, 50)
    print(*a[i])

l1 = int(input("\nInforme a linha que deseja trocar: "))
l2 = int(input(f"Informe por qual linha deseja trocar a linha {l1}: "))

if l1 >= 0 and l1 <= 5 and l2 >= 0 and l2 <= 5:
    for i in range(5):
        a[l2], a[i] = a[l1], a[i]
        a[l1], a[i] = a[l2], a[i]

    print()

    for i in range(5):
        print(*a[i])
else:
    print("Linha inexistente!")