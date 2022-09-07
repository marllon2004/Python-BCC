# O número 3025 tem a seguinte característica:30 + 25 = 55 55^2= 3025. Elabore um programa para mostrar todos os números de 4algarismos que possuem esta mesma característica.

i = 1000

while i <= 9999:
    dezena1 = i // 100
    dezena2 = i % 100

    soma = dezena1 + dezena2

    if soma**2 == i:
        print(i)
    i+=1

