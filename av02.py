#Avaliação 02 - Estrutura de Seleção
'''
Gabriel Barros de Melo Amorim - RA: 574015
Cesar Augusto de Almeida - RA: 626848
Danielle Barros Bassetto - RA: 629391
João Vitor Adonis - RA: 590428
Marllon Silva Araujo Coelho - RA: 627021
Matheus Henrique de Lima - RA: 626732
'''
vai = 0
n1 = int(input('Digite um número de 3 digitos: '))
n2 = int(input('Digite outro número de 3 digitos: '))

soma = n1 + n2

somac = soma//100
somad = soma%100//10
somau = soma%10

n1c = n1//100
n1d = n1%100//10
n1u = n1%10

n2c = n2//100
n2d = n2%100//10
n2u = n2%10

ababa = n1u + n2u
if ababa //10 > 0:
    vai+=1
ababa = ababa //10
ababa = n1d + n2d + ababa
if ababa //10 > 0:
    vai+=1
ababa = ababa//10
ababa = n1c + n2c + ababa
if ababa//10 > 0:
    vai+=1
print(f'{vai} "vai 1"')