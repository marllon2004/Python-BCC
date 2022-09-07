#Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e peça um número ao usuário. Verifique se este número pertence ou não ao vetor. Imprima o vetor e a mensagem de número encontrado ou não.

from random import randint

a = []
qt = 0

for i in range(10):
    a.append(randint(1, 50))

print(a)
n = int(input("Informe um número: "))

for i in range(10):
    if n == a[i]:
        qt += 1

if qt > 0:
    print(f"O número {n} aparece {qt} vez(es) no vetor!")
else:
    print(f"O número {n} NÃO aparece no vetor!")