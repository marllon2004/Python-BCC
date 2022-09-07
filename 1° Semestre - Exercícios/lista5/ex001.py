from random import randint

a = []
par = 0
impar = 0

for i in range(10):
    a.append(randint(1,50))
    if a[i] % 2 == 0:
        par+=1
    else:
        impar+=1
print(a)
print(f"{par} Pares \n{impar} Impares")