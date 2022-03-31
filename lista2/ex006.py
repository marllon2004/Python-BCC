# Sejam três números inteiros diferentes digitados pelo usuário, faça um programa em Pythonque os coloque em ordem crescente.

n1 = int(input("Valor de N1: "))
n2 = int(input("Valor de N2: "))
n3 = int(input("Valor de N3: "))

if n1 > n2:
    n1, n2 = n2, n1

if n2 > n3:
    n2, n3 = n3, n2

if n1 > n2:
    n1, n2 = n2, n1

print(f"{n1} {n2} {n3}")