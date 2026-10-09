n = int(input('Talet n? '))

summa = 0
k=1

while k <= n:
    summa = summa + k*k
    k= k + 1
print(f'Summan blir = {summa}')