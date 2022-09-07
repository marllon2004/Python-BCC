# BITS TROCADOS - As  Ilhas  Weblands  formam  um  reino  independente  nos  mares  do  Pacífico.  Como  é  um  reino recente, a sociedade é muito influenciada pela informática. A moeda oficial é o Bit; existem notas de  B$  50,00,  B$10,00,  B$5,00  e  B$1,00.  Você  foi  contratado(a)  para  ajudar  na  programação  dos caixas automáticos de um grande banco das Ilhas Weblands.
# Os  caixas  eletrônicos  das  Ilhas  Weblandsoperam  com  todos  os  tipos  de  notas  disponíveis, mantendo  um  estoque  de  cédulas  para  cada  valor  (B$  50,00,  B$10,00,  B$5,00  e  B$1,00).  Os clientes do banco utilizam os caixas eletrônicos para efetuar retiradas de um certo número inteiro de Bits.Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo cliente, determine o número  de  cada  uma  das  notas  necessário  para  totalizar  esse  valor,  de  modo  a  minimizar  a quantidade de cédulas entregues. Por exemplo, se o cliente deseja retirar B$50,00, basta entregar uma única nota de cinquenta Bits. Se o cliente deseja retirar B$72,00, é necessário entregar uma nota de B$50,00, duas de B$10,00 e duas de B$1,00.

valor = int(input("Informe o valor a ser retirado: "))

q50 = valor // 50
valor = valor % 50
q10 = valor // 10
valor = valor % 10
q5 = valor // 5
valor = valor % 5
q1 = valor // 1

print(f"NOTAS NECESSÁRIAS: \n"
      f"Notas de B$ 50,00 = {q50} \n"
      f"Notas de B$ 10,00 = {q10} \n"
      f"Notas de B$ 5,00 = {q5} \n"
      f"Notas de B$ 1,00 = {q1}")