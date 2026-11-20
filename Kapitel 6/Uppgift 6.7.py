print('Skriv en matris rad för rad.'
      'avsluta med en tom rad')

m = []

while True:
    s = input('? ')
    if s == '':
        break
    s = s.replace(' ', '')
    ls = s.split(',')
    rad = [float(e) for e in ls]
    m.append(rad)
print(m)
    