#Faça um programa em Python que imprima todos os números primos de um intervalo informado pelo usuário. Utilize o método do exercício 4 para verificar se o número é primo ou não.

def primo(n):
    if n <= 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

ini = int(input("Início: "))
fim = int(input("Fim: "))

if fim < ini:
    ini, fim = fim, ini

for i in range(ini, fim+1):
    if primo(i):
        print(i)