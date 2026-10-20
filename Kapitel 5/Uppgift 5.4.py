s = input("Skriv en text: ")
i = len(s)-1
while i  >= 0:
    if s[i] == ' ' or s[i] == '\t':
        break
    i -= 1
if i > 0:
    print(f'sista vitt tecken är på plats {i:d}')
else:
    print("Det finns ingen vitt tecken")