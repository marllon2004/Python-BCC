from random import randint

a = []
b = []

for i in range(10):
    a.append(randint(1,50))
print(a)
x = int(input("Informe um valor: "))

b = [0]*10

for i in range(10):
    b[i] = a[i] * x
print(b)