# Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# O número digitado ao quadrado
# A raiz quadrada do número digitado

n = int(input("Informe um número: "))

if n >= 0:
    q = n ** 2
    raiz = n ** 0.5

    print(f"Número {n} ao quadrado é: {q} \n"
          f"Raiz quadrada de {n} é {raiz:.1f}")
else:
    print(f"{n} não é um número positivo!")