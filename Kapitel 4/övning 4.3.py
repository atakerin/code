pengar = 0.01
dagar = 0 

while pengar < 10000000:
    pengar *= 2
    dagar += 1

print(f'Det tar {dagar} dagar för att tjäna {round(pengar)} Kr.')