#O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, 'A' seria substituído por 'D', 'B' se tornaria 'E', e assim por diante. Implement um programa que faça uso desse Código de César (3 posições), entre com uma string e retorne a string codificada.

frase = input("Frase: ").upper()

cripto = ""
for i in frase:
    if i.isalpha():
        cripto += chr(ord(i)+3)
    else:
        cripto += i

print(f"String: {frase}")
print(f"Criptografada: {cripto}")