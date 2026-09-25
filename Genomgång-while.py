import time
import math

x = 1
#utskrift av alla tall mellan 1 och 10
while x <= 10:
    print(x)
    x += 1
    
#utskirft av jämna tal
k = 0
while k < 10:
    k += 1
    if k%2 == 0:
        print(k)
        continue
    
#beräkning av summan 1+2+3+..+n
while True:
    n = int(input('n?, skriv ett tall mindre än eller lika med 0 för avsluta:'))
    start = time.time()
    if n <= 0:
        break
    summa = 0
    l = 1
    while l <=n:
        summa += l
        l += 1
    slut = time.time()
    print(f'Summan blir, {summa} Det tog, {round(slut-start)}, sekunder att räkna')