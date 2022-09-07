"""3.Faça um programa que gereduas sequências de números inteiros ordenados e imprima uma  sequência  com  os  números  ordenados  das  duas  sequências  anteriores.
Você  não deve usar o método sortpara oresultado.
Exemplo: Primeira sequência: 1 3 5 5 7 9 10 Segunda sequência: 2 2 4 6 8 8 10 Resultado: 1 2 2 3 4 5 5 6 7 8 8 9 10 10"""

from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(randint(1, 10))
    b.append(randint(1, 10))

c = a+b

for i in range(20):
    for j in range(i+1, 20):
        if c[i] > c[j]:
            c[i], c[j] = c[j], c[i]

print(a)
print(b)
print(c)