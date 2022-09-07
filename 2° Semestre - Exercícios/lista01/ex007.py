#Fazer um programa em Python para verificar se uma determinada String é palíndrome. Exs.: ANA - MUSSUM - OVO

palavra = input("Palavra: ")

if palavra == palavra[::-1]:
    print(f"A palavra {palavra.upper()} é palíndrome.")
else:
    print("Não é palíndrome.")