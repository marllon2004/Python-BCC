lista = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n = int(input())
for i in range(n):
    soma = 0
    v = input()
    for dig in v:
        soma += lista[int(dig)]
    print(f"{soma} leds")
