text = input("Ditt mejl: ")

text = text.lower()
text = text.replace("aa", "å")
text = text.replace("ae", "ä")
text = text.replace("oe", "ö")

print(text)