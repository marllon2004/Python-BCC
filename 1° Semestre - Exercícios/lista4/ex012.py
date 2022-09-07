# Elabore  um  programa  que  calcule  N!  (fatorial  de  N),  sendo  que  o  valor  inteiro  de  N  é fornecido pelo usuário.

n = int(input("Informe o número para saber o fatorial dele: "))

i=1
fat = 1

while i <= n:
    fat = fat * i #faz a multiplicação de tds os números anteriores a N
    i+=1
print(fat)