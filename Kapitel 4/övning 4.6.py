summa = 0
nämnare = 1

while True:
    k = 1 / nämnare
    
    if nämnare %2 == 0:
       k = -k
    if abs(k) < 0.00001:
        break
    
    summa += k
    nämnare += 1
    
print(summa)
