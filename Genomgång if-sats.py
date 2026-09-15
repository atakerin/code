ålder = int(input('Hur gammal är du? '))

if ålder == 17:
    print('Du är lika gammal som de flesta i EE25.')
    
if ålder != 43:
    print('Du är inte lika gammal som Per.')
else:
    print('du är lika gammal som Per.')
    
if ålder <= 13:
    print('du år väldigt ung.')
elif ålder < 18:
    print('Du får inte ta kärkort.')
elif ålder <20:
    print('Du får ta körkort.')
else:
    print('Du får handla på systembolaget.')

namn = input('vad är ditt namn? ')

if namn == 'Atakan' or 'atakan':
    print('Hej Atakan.')
else:
    print('who?')
    
if ålder == 18 and namn == 'Atakan' or 'atakan':
    print('hej atakan, du är 18 år gammal.')
else:
    print(f'Hej {namn}, du är {ålder} år gammal.')