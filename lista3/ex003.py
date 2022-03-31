# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

n1 = int(input("Valor de N1: "))
n2 = int(input("Valor de N2: "))

if n1 > n2:
    print(f"O maior valor é N1: {n1} \n"
          f"Diferença entre N1 e N2 é: {n1 - n2}")

elif n1 == n2:
    print("Números Iguais!")

else:
    print(f"O maior valor é N2: {n2} \n"
          f"Diferença entre N2 e N1 é: {n2 - n1}")
