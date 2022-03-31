# JOGO CAÇA NÍQUEIS - O  programa  deverá  sortear  três  números  aleatórios  (1  a  99)  e  as  seguintes  regras  deverão  ser consideradas: Se nenhum número for igual, o apostador perde o jogo, se dois números forem iguais, o  apostador  ganhará  5  vezes  o  valor  da  aposta,  se  acertar  os  três  ganhará  100  vezes  o  valor  da aposta. Imprimir o valor ganho pelo apostador.
import random

valor = float(input("Informe o valor da aposta em R$: "))
n1 = random.randint(1, 99)
n2 = random.randint(1, 99)
n3 = random.randint(1, 99)

print(f"\nNÚMEROS SORTEADOS: \n"
      f"N1 -> {n1} | N2 -> {n2} | N3 -> {n3} \n")

if n1 != n2 and n2 != n3 and n1 != n3:
    print("VOCÊ PERDEU!!! \n"
          "Números diferentes!")

elif n1 == n2 or n2 == n3 or n1 == n3:
    print(f"2 NÚMEROS IGUAIS!!! \n"
          f"Valor apostado: {valor} \n"
          f"Valor ganho: {valor*5}")

else:
    print(f"3 NÚMEROS IGUAIS!!! \n"
          f"Valor apostado: {valor} \n"
          f"Valor ganho: {valor*100}")