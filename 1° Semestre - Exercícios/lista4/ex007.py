# Escreva um programa que gere um conjunto de 20 números inteiros aleatórios entre 1 e 50 e mostre qual foi o maior eo menor valorgerado.
import random

i = 1
maior = 0
menor = 51

while i <= 20:
    n = random.randint(1, 50)
    print(n,end=" | ")

    if n >= maior:
        maior = n
    if n <= menor:
        menor = n

    i+=1

print(f"\nMaior valor: {maior} \n"
      f"Menor valor: {menor}")