#Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e  50) sem números repetidos. Imprima o vetor.

from random import randint, sample

a = []

'''for i in range(10): #Cria o vetor com os 10 valores aleatórios
    a.append(randint(1, 50))

a.sort() #Coloca o vetor em ordem crescente 

for i in range(len(a)-1): #vai de 1 até o penultimo valor do vetor (pq o ultimo valor n repete)
    if a[i+1] == a[i]: #verifica se o valor sucessor do vetor é igual ao anterior
        a[i] = randint(51, 100) #se for igual, ele coloca outro valor           


a.sort() #Coloca em ordem crescente (facilita a visualização)
print(a)'''

A = list(range(1, 51))
L = sample(A,10)
print(sorted(L))