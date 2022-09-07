p1, c1, p2, c2 = input().split()

p1 = int()
c1 = int()
p2 = int()
c2 = int()

aaa = p1*c1
bbb = p2*c2

if aaa < bbb:
    print("-1")
elif bbb < aaa:
    print("1")
elif aaa == bbb:
    print("0") 