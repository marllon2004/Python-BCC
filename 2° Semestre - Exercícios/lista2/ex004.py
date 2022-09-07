#Escreva um programa em Python que contenha uma função que retorne True caso o argumento passado seja primo e False caso contrario. O argumento será sempre um valor inteiro. Peça um número, chame o método e imprima se o mesmo é número primo ou não.

def primo(a):
    if n <= 1:
        return False
    for i in range(2, a//2+1):
        if n % i == 0:
            return False
    return True


n = int(input("Informe o número: "))

print(primo(n))