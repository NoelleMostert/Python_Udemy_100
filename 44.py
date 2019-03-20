import string

with open("alphathree.txt","w") as file:
    for i, j, k in zip((string.ascii_uppercase[0::3]+" "), (string.ascii_lowercase[1::3]+" "), (string.ascii_lowercase[2::3]+" ")):
        file.write(i + j + k + "\n")