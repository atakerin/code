pn = input("Skrin in ditt personnummer: ")
sist = int(pn[8:9])

if sist % 2 == 0:
    print("kvinna")
else:
    print("man")