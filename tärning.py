import random

dit_slag = random.randint(1,6)

datorn_slag = random.randint(1,6)

print(f"Du slog: {dit_slag}")

print(f"datorn slog: {datorn_slag}")

if dit_slag > datorn_slag:
    print("Du Vann!")
    
elif dit_slag == datorn_slag:
    print("det är  oavgjort ")
    
else:
    print("dator vann den här gången")