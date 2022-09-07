#Implemente um programa para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário

salario = float(input("Informe o salário atual: "))
reajuste = int(input("Informe o percentual do reajuste: "))

ajuste = (salario * reajuste) / 100
novo_salario = salario + ajuste

print(f'Com um ajuste de {ajuste} reais, o novo salário é {novo_salario}')

