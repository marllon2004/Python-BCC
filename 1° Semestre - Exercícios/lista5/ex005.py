from random import randint

a = []
for i in range(10):
    a.append(randint(1,50))
print(a)
op = int(input("ESCOLHA UMA OPÇÃO: \n"
               "[1] -> DIRETA\n"
               "[2] -> INVERSA\n"
               ">> "))
if op == 1:
    print(a)
elif op == 2:
    new = a[::-1]
    print(new)
else:
    print("Opção inexistente")