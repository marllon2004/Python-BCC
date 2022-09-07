#Faça um programa em Python que leia uma String e dois caracteres. Troque todas as ocorr~encias do primeiro caractere (podendo ser maiúsculo ou minúsculo) pelo segundo e imprima a quantiade de vezes que o caractere foi substituído.

frase = input("Frase: ").upper()
letra1 = input("Substituir o caractere: ").upper()
letra2 = input("Por: ").upper()

count = frase.count(letra1)
frase = frase.replace(letra1, letra2)

print(f"Nova frase: {frase}")
print(f"Número de susbtituições: {count}")

