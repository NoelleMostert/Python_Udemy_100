def wcount(filepath):
        with open(filepath, 'r') as file:
                strng = file.read()
                ostrng = strng.replace(",", " ")
                nstrng = ostrng.split(" ")
                return len(nstrng)
print(wcount("words2.txt"))