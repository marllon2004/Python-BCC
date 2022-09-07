from random import randint

a = []
print("Múltiplos de 5: ", end="")
for i in range(20):
    a.append(randint(1,50))
    if a[i] % 5 == 0:
        print(a[i], end=" ")
print(f"\n{a}")