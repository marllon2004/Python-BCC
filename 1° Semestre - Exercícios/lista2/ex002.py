# Elaborar  um  programa  em Pythonpara  ler  somente  a  parte  numérica  da  placa  de  um  carro  e apresentar o dia do rodízio (em SP) para o mesmo (digitar apenas um número com 4 dígitos, fazer a validação).
# 1 ou 2 -> Segunda | 3 ou 4 -> Terça | 5 ou 6 -> Quarta | 7 ou 8 -> Quinta | 9 ou 0 -> Sexta

placa = int(input("Informe a parte númerica da placa do carro: "))

if placa < 1000 or placa > 9999:
    print("Valor icompatível! Informe um número de apenas 4 algarismos!")

else:
    u = placa % 10

    if u == 1 or u == 2:
        print(f"Final {u} -> Rodízio Segunda!")

    elif u == 3 or u == 4:
        print(f"Final {u} -> Rodízio Terça!")

    elif u == 5 or u == 6:
        print(f"Final {u} -> Rodizío Quarta!")

    elif u == 7 or u == 8:
        print(f"Final {u} -> Rodízio Quinta!")

    else:
        print(f"Final {u} -> Rodízio Sexta")