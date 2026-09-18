tid = int(input('Hur länge kommer du att ringa per månad? '))

if tid <= 33:
    print('Abonemangen "Kontant" är best för dig!')
elif tid <= 66:
     print('Abonemangen "normal" är best för dig!')
else:
     print('Abonemangen "plus" är best för dig!')