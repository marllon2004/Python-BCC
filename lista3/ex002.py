# Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

n = int(input("Informe um número: "))

resto = n % 2

if resto == 0:
    print(f"O número {n} é PAR!")

else:
    print(f"O número {n} é ÍMPAR!")