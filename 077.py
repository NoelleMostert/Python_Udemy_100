import datetime

age = input("How old are you:")
now = datetime.datetime.now().year
year_born = int(now) - int(age)
print("We think you were born back in %s" % year_born)