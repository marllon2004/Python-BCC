n = int(input())
nn = n
quant = 0

while n > 0:
    nz = nn // 10
    if nz == 1:
        quant+=2
    elif nz == 7:
        quant+=3
    elif nz == 4:
        quant+=4
    elif nz == 2 or n == 3 or n== 5:
        quant+=5
    elif nz == 6 or n == 0 or n == 9:
        quant+=6
    elif nz == 8:
        quant+=7

print(f"{quant} leds")