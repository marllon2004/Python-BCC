'''
                GRUPO 8
    Marllon Silva Araujo Coelho RA: 627021
    Matheus Henrique de Lima RA: 626732
    Cesar Augusto de Almeida RA: 626848
    Danielle Barros Bassetto RA: 629391
    Gabriel Barros de Melo Amorim RA: 574015
    João Vítor Adonis RA: 590428
'''

n = int(input("Insira o número que deseja saber a tabuada: "))

if n > 0:
    for i in range(1, n + 1):
        for j in range(i, i * n + 1, i):
            print(j, end=' ')
        print()
else:
    print("ERRO! Número menor ou igual a zero.")