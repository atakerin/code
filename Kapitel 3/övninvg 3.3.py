import math

a = float(input('Vad är längden på sidan "a": '))
b = float(input('Vad är längden på sidan "b": '))
c_vinkel = float(input('Vad är vinkeln mellan "a" och "b": '))

radian = math.radians(c_vinkel)
tolerans = 1e-10
c = math.sqrt((a**2 + b**2)-2*a*b*math.cos(radian))


if abs(a - b) < tolerans and abs(b - c) <tolerans and abs(a - c) < tolerans:
    print("triangeln är liksidig")

elif abs(a - b) < tolerans or abs(b - c) <tolerans or abs(a - c) < tolerans:
    print("triangeln är likbent")

else:
    print("Triangeln är oliksidig")
    
print(f'sidan "c" är {c:.5} lång')