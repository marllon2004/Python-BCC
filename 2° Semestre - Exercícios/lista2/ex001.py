#Escreva um programa em Python que contenha uma função que peça um número e verifique se é par ou ímpar. No principal, chame a função.

def parOUimpar(a):
    if a % 2 == 0:
        print("Par")
    else:
        print("Impar")

n = int(input("Informe o número: "))
parOUimpar(n)