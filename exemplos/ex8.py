#Ler dois valores A e B e troca-los. A = B e B = A

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))

toto = a
a = b
b = toto

print(f'Valor de A: {a} \n'
      f'Valor de B: {b}')

