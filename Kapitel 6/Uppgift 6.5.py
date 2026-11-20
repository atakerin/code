namn = []
pris = []
while True:
    s = input('namn och prisa för ett kort: ')
    if s == '':
        break
    s = s.strip()
    i = s.rpartition(' ')
    namn.append(i[0].strip())
    pris.append(float(i[2]))
m = min(pris)
k = pris.index(m)
print(namn[k] + ' är billigast')
print(f'Kostnad: {m:1.2f} kr/månad')