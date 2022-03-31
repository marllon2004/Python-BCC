# Construa um programa que verifique se um número fornecido pelo usuário é primo ou não.

n = int(input("Informe um número: "))

div = 0
for i in range(1, n+1):
    if n % i == 0:
        div += 1

if div > 2:
    print("Nâo é primo!!")
else:
    print("É primo")