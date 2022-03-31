# Escreva um programa para ler 10 números do usuário e calcular a soma dos números pares e a soma dos números ímpares.

i = 1
sPar = 0
sImpar = 0

while i <= 10:
    n = int(input("Informe um número: "))

    if n % 2 == 0:
        sPar = sPar + n
    else:
        sImpar = sImpar + n

    i+=1
    
print(f"Soma dos números pares: {sPar} \n"
      f"Soma dos números impares: {sImpar}")