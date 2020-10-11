#f = open("guido_bio.txt")
#text = f.read()
#f.close()
#print(text)

try:
    with open("guido_bio.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)



oceans = ["Pacific", "Atlantic", "Indian", "Sounthern", "Arctic"]

with open("ocean.txt", 'w') as f:
    for ocean in oceans:
        #f.write(ocean)
        #f.write("\n")
        print(ocean, file=f)

with open("ocean.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)

