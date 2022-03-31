from random import random


n1 = int(input("Informe o número do bicho: "))
n2 = int(input("Informe outro número do bicho: "))

p1 = random.randint(0, 9999)
p2 = random.randint(0, 9999)
p3 = random.randint(0, 9999)
p4 = random.randint(0, 9999)
p5 = random.randint(0, 9999)

g1 = (p1 - 1) % 100 // 4 + 1
g2 = (p2 - 1) % 100 // 4 + 1
g3 = (p3 - 1) % 100 // 4 + 1
g4 = (p4 - 1) % 100 // 4 + 1
g5 = (p5 - 1) % 100 // 4 + 1

print(f"1° Prêmio: {p1:04} - Grupo: {g1:02}")
print(f"2° Prêmio: {p2:04} - Grupo: {g2:02}")
print(f"3° Prêmio: {p3:04} - Grupo: {g3:02}")
print(f"4° Prêmio: {p4:04} - Grupo: {g4:02}")
print(f"5° Prêmio: {p5:04} - Grupo: {g5:02}")

if n1 in [g1, g2, g3, g4, g5] and n2 in [g1, g2, g3, g4, g5]:
    