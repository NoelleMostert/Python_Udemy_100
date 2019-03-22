d = {"a": 1, "b": 2, "c": 3}
x = dict((key,value) for key, value in d.items() if value <= 1)
print(x)