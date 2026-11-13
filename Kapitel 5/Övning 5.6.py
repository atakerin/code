text1 = input("Första text: ")
text2 = input("Andra text: ")

text1 = text1.replace(' ', '').lower()
text2 = text2.replace(' ', '').lower()

if len(text1) != len(text2):
    anagram =False
else:
    anagram = True
    for i in text1:
        an1 = 0
        for x in text1:
            if x == i:
                an1 += 1
        an2 = 0
        for x in text2:
            if x == i:
                an2 += 1
        if an1 != an2:
            anagram = False
            break
if anagram:
    print("anagram")
else:
    print("inte anagram")