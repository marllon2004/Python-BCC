#Converter segundos em horas, minutos e segundos

tempo = int(input("Informe o tempo em segundos: "))

horas = tempo // 100
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60

print(f'{horas} horas e {minutos} minutos e {segundos} segundos')