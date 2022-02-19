# Ler o comprimento e a largura de um terreno retangular e mostrar o perímetro e área

comp = float(input("Informe o comprimento do terreno: "))
larg = float(input("Informe a largura do terreno: "))

perimetro = 2 * (comp + larg)
area = comp * larg

print(f'O perímetro é {perimetro} e a área é {area}')