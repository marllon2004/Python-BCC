from random import randint

a = []
n = int(input("Informe um número: "))
print(f"Números múltiplos de {n}: ", end="")
for i in range(20):
    a.append(randint(1,50))
    if a[i] % n == 0:
        print(a[i], end=" ")
print(f"\n{a}")