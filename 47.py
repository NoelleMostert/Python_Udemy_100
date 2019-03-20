from glob import glob

l = []
check = "python"

for i in glob("letters/*txt"):
    with open (i) as file:
        j = file.read(1)
    if j in check:
        l.append(j)

print(l)