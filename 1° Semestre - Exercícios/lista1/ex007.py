#Implemente um programa para ler o preço do litro do combústivel de um carro, ler o desempenho do veículo (km/l) e a distância entre as duas cidades (km), e informar quantos litros, e quanto dinheiro vai ser gasto para fazer uma viagem entre as  duas cidades

gaso = float(input("Qual o preço da gasolina? "))
desempenho = float(input("Quantos Kilometros por litro o carro faz? "))
km = float(input("Qual distância entre as duas cidades? "))

litros = km / desempenho
dinheiro = litros * gaso

print(f'Quantidade de litros necessários: {litros} \n'
      f'Quantidade de dinheiro previsto para viagem: {dinheiro}')
