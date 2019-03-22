def wcount(filepath):
        with open(filepath, 'r') as file:
                strng = file.read()
                nstrng = strng.split(" ")
                return len(nstrng)
print(wcount("words1.txt"))