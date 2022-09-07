"""4.Faça um programa em Pythonque gere um vetor com N elementos e ordene utilizando o método BubbleSort e pelo método sort.
Faça a comparação de tempo para a ordenação(imprima  o  tempo  de  ordenação  de  cada  método)do  mesmo  conjunto  de  elementos.
 Faça teste para vários valores de N."""

from random import randint
import time


a = []
b = []
c = []

for i in range(100000):
    a.append(randint(1, 10))
    b.append(randint(1, 10))
c = a+b

bubbleSort = time.time()
for i in range(200):
    for j in range(i+1, 20):
        if c[i] > c[j]:
            c[i], c[j] = c[j], c[i]
print(c)
bubbleSortFim = time.time()


sort = time.time()
c.sort()
print(c)
sortFim = time.time()

print(bubbleSortFim - bubbleSort)
print(sortFim - sort)
