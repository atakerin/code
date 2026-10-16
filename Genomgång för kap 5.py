status = 'Godkänt'
print(status)

halsning = 'God '\
    'morgon'
print(halsning, status)

citat = 'Hon sade \'hej\' till alla'
print(citat)

sokvag = 'C:\\användare\\dokument'
print(sokvag)

#Escape-sekvenser (\n \t)
meny = 'Meny:\n\t1. Starta\n\t2. Avsluta'
print(meny)

#Raw String (r-prefix)
filsokvag = r'C:\ny_mapp\test.txt'
print(filsokvag)

#Formatted String Literals (f-string)
pris=3
print(f'Totalt pris: {pris:.2f}kr')

#Flerradig strängar (""")
instruktion = """Välkommen!idag ska vi lära os att programera
    i Python"""
print(instruktion)

#Direkt Unicode
valuta = 'pris:50€'
print(valuta)

#Hex \u kod
t4 ='Spelade \u2665 ess'
print(t4)

#Namngivna n
print('\N{DOLLAR SIGN}')

#chr() & ord()
print(chr(65))
print(ord('A'))

#Indexering & len()
ord = 'Katt'
print(ord[0])
print(ord[-1])
print(len(ord))

#skivor (slicing)
frukt ='apelsin'
name = 'Atakan Ebbhagen'
print(frukt[0:4])
print(frukt[::-1])
print(name[::-1])