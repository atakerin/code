t = (input('skriv några tall: '))

x = t.split()
tal = [int(f) for f in x]
negativ = [f for f in tal if f < 0]
print(len(negativ))