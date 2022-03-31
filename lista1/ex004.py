#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total de segundos

dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a qunatidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

conversao_dias = ((dias * 24) * 60) * 60
conversao_horas = (horas * 60) * 60
conversao_minutos = minutos * 60
total = conversao_dias + conversao_horas + conversao_minutos + segundos

print(f'{dias} dias, {horas} horas, {minutos} minutos, {segundos} convertido para segundos é {total}')