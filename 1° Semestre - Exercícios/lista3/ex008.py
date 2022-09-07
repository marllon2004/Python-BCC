# Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe  naquele  mês.  Note  que  Fevereiro  tem  29  dias  em  anos  bissextos,  e  28  dias  em  anos  não bissextos.

d = int(input("Informe o dia: "))
m = int(input("Informe o mês: "))
a = int(input("Informe o ano: "))

if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and (d >= 1 and d <= 31):
    print(f"{d}/{m}/{a} --> Data Válida!")

elif (m == 4 or m == 6 or m == 9 or m == 11) and (d >=1 and d <= 30):
    print(f"{d}/{m}/{a} --> Data Válida!")

elif m == 2 and a % 4 == 0 and d >= 1 and d <= 29:
    print(f"{d}/{m}/{a} --> Data Válida!")

elif m == 2 and a % 4 != 0 and d >=1 and d <= 28:
    print(f"{d}/{m}/{a} --> Data Válida!")

else:
    print(f"{d}/{m}/{a} --> Data INVÁLIDA!")