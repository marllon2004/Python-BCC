from random import randint

a = []
par = 0
media = 0

for i in range(20):
    a.append(randint(1,50))
    if a[i] % 2 == 0:
        par += 1
        media += a[i]
print(a)
print(f"Média dos números PARES: {media/par:.2f}")