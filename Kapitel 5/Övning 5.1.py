a = input("skiv minst två ord: ")

a = a.strip()
b = a.find(' ')
c = a.rfind(' ')

print(a[0:b])
print(a[c+1:])