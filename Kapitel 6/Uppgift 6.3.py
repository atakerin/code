import random
l = list()
mid = 0
for i in range(1, 100):
    r = random.randint(1,1000)
    l.append(r)
    mid += r
print(l)
print(f'minsta talet: {min(l)}')
print(f'största talet: {max(l)} ')
print(f'medelvärde: {mid/len(l):1.1f}')