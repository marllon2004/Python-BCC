# Escreva um programa que peça a Nota 1 (N1) e a Nota 2 (N2) de 10 alunos e a cada aluno mostre a média M, onde M=(N1+N2)/2.

a = 1

while a <= 10:
    n1 = float(input("Informe a 1º nota: "))
    n2 = float(input("Informe a 2º nota: "))

    m = (n1+n2)/2

    print(f"A média no {a}º aluno é {m} \n")
    a+=1