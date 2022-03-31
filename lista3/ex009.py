#Uma receita para produzir um bolo conta com 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de leite (estes dados são constantes nesta receita). Você deve escrever um programa em Pythonque dados  como  entrada  A  (quantidade  de  xicaras  de  farinha  de  trigo),  B  (quantidade  de  ovos)  e  C (quantidade de colheres de leite) todos valores inteiros, o programa deve mostrar quantos bolos podem ser produzidos.

trigo = int(input("Informe a quantidade de xícaras de trigo: "))
ovos = int(input("Informe a quantidade de ovos: "))
leite = int(input("Informe a quantidade de colheres de leite: "))

if trigo >= 2 and ovos >= 3 and leite >= 5:
    trigo = trigo // 2
    ovos = ovos // 3
    leite = leite // 5

    if trigo == ovos and ovos == leite:
        print(f"Produzirá {trigo} bolos!")

    else:
        if trigo <= ovos and ovos <= leite:
            print(f"Produzirá {trigo} bolos!")

        elif ovos <= trigo and trigo <= leite:
            print(f"Produzirá {ovos} bolos!")

        else:
            print(f"Produzirá {leite} bolos!")