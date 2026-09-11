import math

S = float(input("Hur många År?:"))
T = 5730
lam = math.log(2) / T

Procent_kvar = math.exp(-lam * S) * 100

print(f'Efter {S} år återstårs {Procent_kvar} % av isotop c14 ')