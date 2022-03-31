# Anotafinaldeumestudante é calculadaapartirdetrêsnotasatribuídasentreointervalo de 0 até10, respectivamente, a um trabalho de laboratório, a uma avaliaçãosemestral e a um exame final. A média  das  três  notas  mencionadas  anteriormente  obedece  aos  pesos:  Trabalho  de  Laboratório:  2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno estáreprovado  (média  entre  0  e  2.9),de  recuperação(entre  3  e  4.9)  ou  se  foi  aprovado.  Façatodas  as verificacões necessárias.

trab = float(input("Nota do Trabalho de Laboratório: "))
ava = float(input("Nota da Avaliação Semestral: "))
exame = float(input("Nota do Exame Final: "))

if trab >= 0 and trab <= 10 and ava >= 0 and ava <= 10 and exame >= 0 and exame <= 10:
    media = (trab*2 + ava*3 + exame*5) / 10

    if media >= 0 and media < 3:
        print(f"Aluno Reprovado! \n"
              f"Média: {media}")
    elif media >= 3 and media < 5:
        print(f"Aluno de Recuperação! \n"
              f"Média: {media}")
    else:
        print(f"Aluno Aprovado! \n"
              f"Média: {media}")

else:
    print("Notas inválidas! Informe notas de 0 até 10")


