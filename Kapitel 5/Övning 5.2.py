import datetime

dt = datetime.datetime.now()
dag = dt.date()
d =  str(dag)
pn = input("skriv in ditt personnummer: ")


if pn[2:4] == d[5:7] or pn[4:6] == d[8:10]:
    print("Grattis!")
else:
    print("Du Fyller inte år")