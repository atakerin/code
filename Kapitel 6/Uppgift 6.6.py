num2 = int(input('till vilken tall i tabbellen: '))

a = []

for i in range(0,num2):
    a.append([])
    for j in range(0, num2):
        a[i].append((i+1)*(j+1), )

for rad in a:
    print(f'{rad}')
