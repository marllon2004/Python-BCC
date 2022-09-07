# Uma  forma  de  verificar  se  um  número  é  um  quadrado  perfeito  é  calculando  a  soma  dos números ímpares
# Elabore um programa que leia um número inteiro e verifique se ele é ou não quadrado perfeito.

n = int(input("Informe um número: "))

raiz = n**0.5

if raiz**2 == n:
    print(f"O número {n} é um quadrado perfeito!!!")
else:
    print(f"O número {n} NÃO é um quadrado perfeito!!!")

