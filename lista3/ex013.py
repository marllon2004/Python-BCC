# Leia 2 valores com casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

x = float(input("Informe um valor: "))
y = float(input("Informe outro valor: "))

if x == 0 and y == 0:
    print("Origem")

elif x == 0:
    print("Eixo Y")

elif y == 0:
    print("Eixo X")

elif x > 0 and y > 0:
    print("Q1")

elif x < 0 and y > 0:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")

else:
    print("Q4")