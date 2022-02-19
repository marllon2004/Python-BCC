# Ler o preço de um produto e mostrar o novo preço com 10% de desconto

preco = float(input("Informe o preço do produto: "))

desconto = (preco * 10) / 100
novo_preco = preco - desconto

print(f'O novo preço do produto é {novo_preco}')