"""1.Faça  um  programa  que geredois  conjuntos  de  números  inteiros  distintos  e  imprima  a interseção  destes  dois  conjuntos
(os  números  presentes  em  ambos  os  conjuntos).
 Exemplo:
 Primeiro conjunto: 1 2 3 4 5
 Segundo conjunto: 2 5 7 1 9 18
 Resultado: 1 2 5 5"""

from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(randint(1,10))
    b.append(randint(1, 10))


for i in range(10):
    for j in range(10):
        if a[i] == b[j]:
            c.append(a[i])

a.sort()
b.sort()

print(a)
print(b)
print(c)

