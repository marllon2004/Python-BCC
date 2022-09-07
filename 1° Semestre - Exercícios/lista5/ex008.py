#Faça  um  programa  em Pythonque  gere  20  elementos  aleatórios  (entre  1  e  50) armazenando no vetor A e crie outros 2 vetores B e C. O vetor B deve ter apenas os números pares e o vetor C deve conter apenas os números ímpares. Imprima os três vetores.

from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(randint(1, 50))

    if a[i] % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

print(f"Vetor: {a}")
print(f"Par: {b}")
print(f"Impar: {c}")