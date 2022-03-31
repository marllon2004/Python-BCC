#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

km = float(input("Quantos kilometros percorridos? "))
dias = int(input("Quantos dias o carro foi alugado? "))

preco = (dias * 60) + (km * 0.15)

print(f'O total a pagar é {preco}')