# Ler um número de no máximo 3 algarismos e mostrar cada número separado

n = int(input("Informe um número: "))

centena = n // 100
dezena = (n // 10) % 10
unidade = n % 10

print(f'Centena: {centena} \n'
      f'Dezena: {dezena} \n'
      f'Unidade: {unidade}')

