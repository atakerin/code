största = 0
minsta = 0
    
while True:
    tal = float(input('Skriv ett positivt tal (negative för att avsluta): '))
    
    if tal <= 0:
        break
    if största == 0:
        största = tal
        minsta = tal
    else:
        if tal > största:
            största = tal
        if tal < minsta:
            minsta = tal
if största != 0:
    print(f'största tall är, {största}')
    print(f'minsta tall är {minsta}')
else:
    print('ingen positiva tal va skriven.')