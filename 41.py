'''import string

f= open("alphabet.txt","w+")

for a in string.ascii_lowercase:
    f.write("%s\n"%a)

f.close()'''

import string
 
with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
