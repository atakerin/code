hojd = float(input('från vilket höjd släps bollen?: '))
studs = 0

while hojd > 0.01:
    hojd *= 0.7
    studs += 1
print(f'Bollen studsar {studs} gånger.')