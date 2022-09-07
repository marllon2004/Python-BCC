# Façaum programa em Python que gere as 5 notas (de 0 a 10) de 10 atletas em uma competição. Armazene em uma matriz 10x5. Após, calcule a média de cada atleta descartando a maior e menor nota obtida e diga qual atleta venceu a competição, ou seja, o número da linha.

from random import randint

a = [0] * 10
media = []
win = 0

for i in range(10):
    a[i] = [0] * 5
    for j in range(5):
        a[i][j] = randint(1, 10)

for i in range(10):
    print(*a[i])

for i in range(10):
    menor = a[i][0]
    maior = a[i][0]
    soma = 0
    for j in range(5):
        if a[i][j] <= menor:
            menor = a[i][j]
        if a[i][j] >= maior:
            maior = a[i][j]
        soma += a[i][j]
    media.append((soma - (menor + maior)) // 3)
print(f"\n{media}")

for i in range(10):
    if media[i] > win:
        win = media[i]
        pos = i

print(f"Vencedor número: {pos}")