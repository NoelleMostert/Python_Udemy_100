def string():
    item = input("Please type a sentence:")
    newitem = item.split()
    newitemcount = len(newitem)
    print("The number of words in your sentence is:%s" % newitemcount)
string()