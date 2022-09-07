# JOGO DA ROLETA - O programa deverá sortear um número aleatório e as seguintes regras deverão ser consideradas:
# Se o apostador acertar o número, imprimir o valor ganho sendo 5 vezes o valor apostado;
# Caso ele erre, mas acertar a dúzia, isto é, Número da Aposta estiver entre (1 e 12) e o Número Sorteado também estiver entre (1 e 12) ou Número da Aposta estiver entre (13 e 24) e o Número Sorteado também estiver entre (13 e 24) ou Número da Aposta estiver entre (25 e 36) e o Número Sorteado também estiver entre (25 e 36), imprimir o valor ganho sendo 3 vezes o valor da aposta;
# Caso ainda erre, mas acertar a paridade, isto é, o Número da Aposta é par e o Número Sorteado também for par ou Número da Aposta é ímpar e o Número Sorteado também for ímpar, imprimir o valor ganho sendo o dobro do valor da aposta.
# Caso erre ainda, ele perde a quantia apostada.
import random   # IMPORTA A BIBLIOTECA PARA GERAR UM NÚMERO ALEATÓRIO

valor = float(input("Informe o valor da sua aposta: "))
n = int(input("Informe o número a ser apostado: "))

x = random.randint(1, 36)   # GERA UM NÚMERO ALEATÓRIO DE 1 A 36 NA VÁRIAVEL X

print(f"\nNúmero Sorteado: {x} \n")

if n == x:
    print(f"PARABÉNS!!! \n"
          f"Valor apostado: {valor} \n"
          f"Valor ganho: {valor*5}")

elif ((n-1) // 12) == (x-1 // 12):
    print(f"ACERTOU A DÚZIA!!! \n"
          f"Valor apostado: {valor} \n"
          f"Valor ganho: {valor*3}")

elif (n % 2 == 0 and x % 2 == 0) or (n % 2 != 0 and x % 2 != 0):
    print(f"ACERTOU A PARIDADE!!! \n"
          f"Valor apostado: {valor} \n"
          f"Valor ganho: {valor*2}")

else:
    print(f"VOCÊ PERDEU!!!")