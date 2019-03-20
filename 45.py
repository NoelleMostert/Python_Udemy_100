import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")

for i in string.ascii_lowercase:
    with open ("letters/"+ i + ".txt", "w") as file:
        file.write(i + "\n")
