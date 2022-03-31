# Elabore  um  programa  para  mostrar  a  sequência  dos  N  primeiro  números  da  série  de Fibonacci: 1   1   2   3   5   8   13   21   34   55   89 ....

n = int(input("Informe até que número deseja ver a sequência de Fibonacci: "))

c = 1
n1 = 0
n2 = 1

print(n2, end=" ") #printa o 1º valor

while c <= n:
    soma = n1 + n2 #soma os 2 últimos números

    print(soma, end=" ")

    n1 = n2 #troca os valores, fazendo o n1 valer o penultimo número
    n2 = soma #faz o n2 valer o último valor da soma
    c+=1