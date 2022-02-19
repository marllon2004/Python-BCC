# Ler o salário de um funcionario, o total valor das venda e mostrar o novo salário com a comissçao de 4%

salario = float(input("Informe o salário bruto: "))
vendas = float(input("Informe o valor total das vendas: "))

comissao = (4 * vendas) / 100
novo_salario = salario + comissao

print(f'Com a acréscimo de 4% da comissão {comissao}, o novo salário é {novo_salario}')