#Escreva um programa em Python que implemente uma função potência, que receba uma base e um expoente por parâmetro e retorne o valor da base elevada ao expoente. O expoente é sempre maior ou igual a zero, e os números são sempre inteiros. Peça uma base e um expoente, chame a função e imprima o resultado

def expoente(a, b):
    exp = 1
    if b < 0:
        print("Expoente deve ser maior ou igual a 0!")
    else:
        for i in range(b):
            exp =  exp * a
        return exp

n1 = int(input("Número Base: "))
n2 = int(input("Número Expoente: "))

print(expoente(n1, n2))