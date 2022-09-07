# Calcule as raízes da equação de 2o grau. E 𝑎𝑥2+𝑏𝑥+𝑐=0representauma equaçãode 2ºgrau.A variável atem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não éequação de segundo grau”.

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

if a == 0:
    print("Não é uma equação do segundo grau!")

else:
    delta = b**2 - 4*a*c
    x1 = ((-b) + (delta**0.5)) / (2*a)
    x2 = ((-b) - (delta**0.5)) / (2*a)

    if delta < 0:
        print(f"Delta < 0 ({delta}). Não existe raiz!")

    elif delta == 0:
        print(f"Delta = 0. Raiz única! \n"
              f"X = {x1}")

    else:
        print(f"As duas raizes são: \n"
              f"X1 = {x1} \n"
              f"X2 = {x2}")