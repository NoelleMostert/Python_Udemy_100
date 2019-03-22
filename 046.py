from glob import glob

l = []

for i in glob("letters/*txt"):
    with open (i) as file:
        l.append(file.read(1))

print(l)