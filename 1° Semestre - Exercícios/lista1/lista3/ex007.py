# Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

km = int(input("Informe a distância do percurso (Km): "))
gaso = int(input("Quantos litros o carro consumiu durante o percurso? "))

litros = km/gaso

if litros < 8:
    print("Venda o carro!")

elif litros >= 8 and litros < 14:
    print("Econômico!")

else:
    print(f"Super econômico!")