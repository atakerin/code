
vald_år = int(input('Vilket År?: '))

befolkning = 26000
start = 2022

while start < vald_år:
    föd = befolkning * 0.007
    död = befolkning * 0.006    
    
    befolkning = befolkning + föd - död + 300 - 325
    start += 1

print(f'I år {vald_år} kommer befålkningen vara {round(befolkning)}')