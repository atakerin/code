text = input("Din text här: ")
konsonanter = "bcdfghjklmnpqrstvwxz"
x = ""

for i in text:
    l = i.lower()
    if l in konsonanter:
        x += l + "o" + l
    else:
        x += l
print(x)