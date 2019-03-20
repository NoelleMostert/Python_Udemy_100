# a = ["1", 1, "1", 2]
# a = set(a)
# print(list(a))
# print(list(set(a)))
# print(list(set(a))) does not keep order of list, testing with [2,"1",1,"1"] will show this

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print (a)
# the above will preserve the order of the list

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
# using a for loop wit an append will also maintain the original list order

