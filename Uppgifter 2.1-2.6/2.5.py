import math

print("Vad Är Kordinaterna för punk 1?")
x1 = float(input("x1: "))
y2 = float(input("y2: "))

print("Vad Är Kordinaterna för punk 2?")
x2 = float(input("x2: "))
y1 = float(input("y1: "))

s = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f'avståndet mellan punkterna är: {s}')