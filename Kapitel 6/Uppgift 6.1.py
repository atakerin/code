tal = int(input('hur många tal? '))

k = 3
f = [2]
for i in range(1, tal):
    f += [f[i-1] * k]
print(f)