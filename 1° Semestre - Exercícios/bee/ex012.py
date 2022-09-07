h, m = input().split()
h = int(h)
m = int(m)

h1 = h // 30
m1 = m // 6

print(f"{h1:02}:{m1:02}")