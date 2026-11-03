text = input("Din text här: ")
konsonanter = "bcdfghjklmnpqrstvwxz"
x = 0

while x < len(text):
    print(text[x], end='')
    t = text[x].lower()
    if t in konsonanter:
        x += 3
    else:
        x += 1