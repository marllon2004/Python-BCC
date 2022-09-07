# Faça  um  programa  para  ler  2  valores,  calcular  e  escrever  a  soma  dos  inteiros  existentes entre os 2 valores lidos (incluindo os valores lidos na soma). O programa deve validar que o 1º  valor  informado  seja  menor  que  o  2º  valor.  O  programa  deve  permitir  que  o  usuário possa executá-lo novamente.

i = 1

while i != 0:
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe outro número: "))

    soma = 0

    if n1 <= n2:
        while n1 <= n2:
            soma = soma + n1
            n1+=1
    else:
        print("[ERROR]\nO 1º VALOR TEM QUE SER MENOR QUE O SEGUNDO!!!!")

    print(f"\nSoma: {soma} \n")

    i = int(input("Deseja continuar? [0 - NÃO / 1 - SIM] -> "))

