n = int(input("Informe o tamanho da matriz: "))

caracol = [0]*n
for i in range(n):
    caracol[i] = [0]*n

c = 1
ini = 0
fim = n

while c <= n**2:
    for i in range(ini, fim):
        caracol[ini][i] = c
        c += 1

    for i in range(ini+1, fim):
        caracol[i][fim-1] = c
        c += 1

    for i in range(fim-2, ini-1, -1):
        caracol[fim-1][i] = c
        c += 1

    for i in range(fim-2, ini, -1):
        caracol[i][ini] = c
        c += 1

    ini += 1
    fim -= 1

for i in range(n):
    for j in range(n):
        print(f'{caracol[i][j]:3}', end = ' ')
    print()