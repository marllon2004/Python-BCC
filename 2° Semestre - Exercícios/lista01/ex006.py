#Escreva um programa em Python que leia uma palavra fornecida pelo teclado e em seguida escreva o caractere presente no meio da palavra, caso esta tenha um número ímpar de caracteres e os dois do meio caso esta tenha um número par de caracteres. Como exemplo, considere a palavra SONHO. O caractere a ser impresso será o N.

palavra = input("Palavra: ")

meio = len(palavra)//2

if len(palavra)%2 == 0:
    print(f"{palavra[meio-1]}{palavra[meio]}")
else:
    print(palavra[meio])