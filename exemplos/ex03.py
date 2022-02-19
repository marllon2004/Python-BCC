#Ler a distância em KM e a velocidade e calculara o tempo de viagem

distancia = float(input("Distância em Km: "))
velocidade = float(input("Velocidade média em Km/h: "))

tempo = distancia / velocidade

print(f'O tempo de viagem previsto é {tempo:.2f} minutos')
