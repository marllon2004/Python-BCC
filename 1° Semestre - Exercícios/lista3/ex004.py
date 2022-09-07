# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que  20%  do  salário  imprima: Empréstimo  não  concedido,  caso  contrário  imprima:  Empréstimo concedido.

sal = float(input("Informe o salário: "))
emprestimo = float(input("Informe o valor da prestação do empréstimo: "))

if emprestimo > sal*0.20:
    print("Empréstimo não concedido! Valor maior que 20% do salário bruto!")

else:
    print("Empréstimo concedido!")