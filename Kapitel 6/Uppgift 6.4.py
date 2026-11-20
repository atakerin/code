l = input("Ange heltal separerade med mellanslag: ")
ls = [int(x) for x in l.split()]

while 0 in ls:
    ls.remove(0)  

print("Listan utan nollor:", ls)
