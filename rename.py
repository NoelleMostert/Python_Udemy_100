# import shutil
# import os

# sourcedir = "C:/Users/Noelle.Mostert/Documents/Python_Udemy"; extensions = (".py")
# files = [(f, f[f.rfind("."):], f[:f.rfind(".")]) for f in os.listdir(sourcedir)if f.endswith(extensions) and f[0].isdigit()]
# maxlen = len(max([f[2] for f in files], key = len))

# for item in files:
#     zeros = maxlen-len(item[2])
#     shutil.move(sourcedir+"/"+item[0], sourcedir+"/"+str(zeros*"0")+item[0])

# import shutil
# import os

# sourcedir = "C:/Users/Noelle.Mostert/Documents/Python_Udemy"
# extensions = (".py")

# files = os.listdir(sourcedir)
# for item in files:
#     if item.endswith(extensions) and item[0].isdigit():
#         name = item.split(".")
#         zeros = 3-len(name[0])
#         newname = str(zeros*"0")+name[0]+"."+name[1]
#         shutil.move(sourcedir+"/"+item, sourcedir+"/"+newname)

#MY FINAL SOLUTION

import os

sourcedir = "C:/Users/Noelle.Mostert/Documents/Python_Udemy_100"
extensions = (".py")

files = os.listdir(sourcedir) #finds the files in the source directory provided
for item in files:
    if item.endswith(extensions) and item[0].isdigit(): #checks if the file is a .py file and starts with a digit at index 0 of the filename
        name = item.split(".") # creates a list object of the split file names
        # print(name)
        zeros = name[0].zfill(3) #add leading zeroes to index one of the created list name
        # print (zeros)
        os.rename(item, zeros + "." + name[1]) #rename the full filename by using the list and changes to the list