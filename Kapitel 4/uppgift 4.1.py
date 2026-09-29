print('[', end='')
k = 0
while k < 6:
    print(f'{k:2}',end='')
    k = k+2
print(' ]')

#om man ändrar start värden, den räknar den nya k värdet + 2
print('[', end='')
k = 1
while k < 6:
    print(f'{k:2}',end='')
    k = k+2
print(' ]')

# om man flyttar på print(' ]') in till loopen så ger den varge nummer en "]"
print('[', end='')
k = 0
while k < 6:
    print(f'{k:2}',end='')
    k = k+2
    print(' ]')

# om man 
print('[', end='')
k = 0

while k < 6:
    print(' ]')
    print(f'{k:2}',end='')
    k = k+2
