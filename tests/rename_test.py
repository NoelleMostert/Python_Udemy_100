import os

sourcedir = "C:/Users/Noelle.Mostert/Documents/Python_Udemy/tests"
extensions = (".py")

files = os.listdir(sourcedir) #finds the files in the source directory provided
for item in files:
    if item.endswith(extensions) and item[0].isdigit(): #checks if the file is a .py file and starts with a digit at index 0 of the filename
        name = item.split(".") # creates a list object of the split file names
        # print(name)
        zeros = name[0].zfill(2) #add leading zeroes to index one of the created list name
        # print (zeros)
        os.rename(item, zeros + "." + name[1]) #rename the full filename by using the list and changes to the list