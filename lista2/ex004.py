# Escreva um programa em Python que leia o valor de 3 lados de um triângulo e escreva se o triângulo é equilátero, isósceles ou escaleno. Faça a validação para verificar se os valores dos lados formam um triângulo.
# Todos os lados tem que ser menor que a soma dos outros dois.

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a < b+c and b < a+c and c < a+b:
    if a == b and a == c:
        print("Triângulo Equilátero")

    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")

    else:
        print("Triângulo Escaleno")

else:
    print("Os valores não formam um triângulo")