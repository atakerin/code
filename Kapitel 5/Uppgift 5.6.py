a = input('Skriv ett svenskt datum som åå/mm/dd: ')

manad = a[3:5]
dag = a[6:]
ar = a[:2]

s =  manad + '/' + dag + '/' + '20' + ar

print(s)