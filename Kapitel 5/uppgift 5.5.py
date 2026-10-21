s = input("Skriv en text: ")
for i in range(0,len(s)):
    
    if s[i] == ' ' or s[i] == '\t':
        print(f'första vitt tecken är på plats {i:d}')
        break
else:
      print("Det finns ingen vitt tecken")