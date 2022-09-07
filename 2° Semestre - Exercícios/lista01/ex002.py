#Faça um programa em Python que leia uma frase e imprima quantas vogais tem esta frase. Considerar minúscula e maiúscula

frase = input("Frase: ").upper()
count = 0
vogais = ["A", "E", "I", "O", "U", "Ã"]
for i in range(len(frase)):
    if frase[i] in vogais:
        count += 1

print(f"Quantidade de vogais: {count}")