a = input('skriv här(små bokstväver): ')
a = a.replace(' ', '')
a = a.lower()
b = a[::-1]

if b == a:
    print('Det är en palindrom')
else:
    print('Det är INTE en palindrom')