# Escreva um programa em Pythonque leia o valor de 3 ângulos de um triângulo eescreva se o triângulo é acutângulo, retângulo ou obtusângulo.
# Faça a validação para verificar se a soma dos ângulos é igual a 180;

a = int(input("Informe o ângulo A: "))
b = int(input("Informe o ângulo B: "))
c = int(input("Informe o ângulo C: "))

if a+b+c == 180:
    if a == 90 and a != b and a != c or b == 90 and b != a and b != c or c == 90 and c != a and c !=b:
        print("Triângulo Retângulo!")

    elif a > 90 and a != b and a !=c or b > 90 and b !=a and b != c or c > 90 and c !=a and c != b:
        print("Triângulo Obtuso!")

    else:
        print("Triângulo Acutângulo!")
else:
    print("As soma dos ângulos não é igual a 180. Portanto, não é um triângulo!")