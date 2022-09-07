#Faça um programa em Python que implemente uma função INVERTE que receba um número como parâmetro e retorne este número escrito ao contrário. Ex: 4312 -> 2134. Peça um número, chame a função e imprima o resultado.

def inverte(a):
    a = int(str(a)[::-1])
    return a

n = int(input("Informe o número: "))

print(inverte(n))
