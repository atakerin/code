import math

pi = math.pi
r = float(input('vad är radien på cirkeln?: '))

area = pi*(r**2)
omkrets = (2*pi)*r

if r > 0:
    print(f'arean är: {area:.5} och {omkrets:.5} ')
else:
    print('skriv ett nummer som är större än 0.')