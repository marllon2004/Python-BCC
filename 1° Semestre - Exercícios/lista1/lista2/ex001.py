# Elabore um programa em Python que leia um número (de 3 algarismos, faça a validação para aceitar apenas  números  menores  que  1000)  e imprima  se  ele  é  ascendente.  Um  número  é  ascendente  se seus algarismos estão em ordem crescente. Por exemplo, o número 258 é ascendente, pois, 2 < 5 e 5 < 8.

n = int(input("Informe um número de 3 algarismos: "))

if n < 99 or n > 999:
    print("Valor imcompatível! Informe somente números de 3 algarismos")

else:
    c = n // 100
    d = n // 10 % 10
    u = n % 10

    if c < d and d < u:
        print(f"{n} é um número ascendente!")

    else:
        print(f"{n} não é um número ascendente!")