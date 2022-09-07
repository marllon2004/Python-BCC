#Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante.

palavra = input("Palavra: ")

ascii = []
convertido = ""

for i in palavra:
    ascii.append(ord(i)+1)

for i in ascii:
    convertido += chr(i)
print(convertido)