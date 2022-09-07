#Elabore um programa em Python que declare uma matriz quadrada de 10 linhas por 10 colunas e verifique se a matriz é simétrica em relação à diagonal principal. A matriz simétrica é aquela em que todos os elementos A(i, j) = A(j, i) para quaisquer valores de i e j. Assim, A[2,1] deverá ser igual a A[1,2], e A[3,5] deverá ser igual a A[5,3] e assim por diante. Imprimir mensagem "Matriz Simétrica" ou "Matriz não Simétrica"

from random import randint

a = [0]*10
La = []
Ca = []

for i in range(10):
    a[i] = [0]*10
    for j in range(10):
        a[i][j] = randint(1, 10)
    print(*a[i])

for i in range(10):
    for j in range(10):
        La.append(a[j][i])
        Ca.append(a[i][j])

if La == Ca:
    print("\nMatriz Simétrica")
else:
    print("\nMatriz não Simétrica")

