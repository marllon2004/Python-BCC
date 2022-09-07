i = 1
par = 0
impar = 0
pos = 0
neg = 0

while i <= 5:
    n = int(input()) 

    if n % 2 == 0:
        par+=1
    if n % 2 != 0:
        impar +=1
    if n > 0:
        pos += 1
    if n < 0:
        neg += 1
    i+=1
    
print(f"{par} valor(es) par(es) \n{impar} valor(es) impar(es) \n{pos} valor(es) positivo(s) \n{neg} valor(es) negativo(s)")