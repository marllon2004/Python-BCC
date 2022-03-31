n = int(input("Informe a quantidade de linhas: "))

for i in range(1, n+1):
    for j in range(i, i**2+1, i):
        print(j, end=" ")
    print()
