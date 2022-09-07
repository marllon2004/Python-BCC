# Igual ao exercício anterior, mas pedir antes do laço a quantidade de números a serem lidos.

quant = int(input("Informe a quantidade de números a serem somados: "))

i = 1
sPar = 0
sImpar = 0

while i <= quant:
    n = int(input("Informe um número: "))

    if n % 2 == 0:
        sPar = sPar + n
    else:
        sImpar = sImpar + n

    i += 1

print(f"Soma dos números pares: {sPar} \n"
      f"Soma dos números impares: {sImpar}")