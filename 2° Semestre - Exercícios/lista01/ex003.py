#Faça um programa em Python que leia uma String e um caractere. Informe a quantidade de vezes que o caractere aparece na string (podendo ser maiúscula ou minúscula)

frase = input("Frase: ").upper()
letra = input("Caractere: ").upper()

count = 0

for i in range(len(frase)):
    if frase[i] == letra:
        count += 1

print(f"Número de ocorrências do caractere {letra} na frase: {count}")