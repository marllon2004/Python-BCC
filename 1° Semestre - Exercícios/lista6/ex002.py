"""2.Faça um  programa  que gere dois  conjuntos  de  números  inteiros  distintos  e  imprima  a união  destes  conjuntos
(os  números  presentes  em  pelo  menos  um  dos  conjuntos).
Exemplo: Primeiro conjunto: 1 2 3 4 5 Segundo conjunto: 2 5 7 1 9 18 Resultado: 1 2 3 4 5 7 9 18 6"""

from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(randint(1, 10))
    b.append(randint(1, 10))

for i in range(10):
  if a[i] not in b and a[i] not in c:
    c.append(a[i])

a.sort()
b.sort()
c.sort()

print(f'{a}'
      f'\n{b}'
      f'\n{c}')