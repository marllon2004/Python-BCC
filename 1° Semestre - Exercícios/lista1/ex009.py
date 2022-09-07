# Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius: C = ((F - 32)/9)*5

F = float(input("Informe a temperatura em Fahrenheit: "))

C = ((F - 32)/9)*5

print(f'Conversão de {F} graus Fahrenheit para Celisus é: {C:.2f} graus celsius')