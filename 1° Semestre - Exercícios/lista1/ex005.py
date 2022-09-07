#Escreva um programa que armazene um valor de entrada em uma variável A e outro em uma variável B. A Seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. Ao final escrever os valores que ficaram armazenados nas variáveis.

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

c = a
a = b
b = c

print(f'Valor de A: {a} \n'
      f'Valor de B: {b}')