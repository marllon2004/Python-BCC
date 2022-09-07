# Faça um programa em Pythonque lê um conjunto de 3 valores op, base, altura, onde op é um valor inteiro e positivo e base e altura, são quaisquer valores reais. A seguir:
# a)Se op=1 calcular e imprimir a área de um retângulo Area=base*altura.
# b)Se op=2 calcular e imprimir a área de triângulo Area=(base*altura)/2.

b = float(input("Informe a base: "))
alt = float(input("Informe a altura: "))
print("Agora escolha uma das opções abaixo!")
print("Opção 01 - Calcular a área de um Retângulo")
print("Opção 02 - Calcular a área de um Triângulo")
op = int(input("Informe o número da sua opção: "))

if op == 1:
    a = b * alt
    print(f"Área do Retângulo é {a}")

elif op == 2:
    a = b * alt / 2
    print(f"Área do Triângulo é {a}")
