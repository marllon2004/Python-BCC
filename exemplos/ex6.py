#Ler um valor em reais (R$) e mostrar a conversão a conversão para o dólar ($)

reais = float(input("Informe o valor em reais: R$ "))
dolar = float(input("Informe a cotação do dólar: $ "))

conversao = reais / dolar

print(f'O valor convertido de real para dólar é: $ {conversao}')