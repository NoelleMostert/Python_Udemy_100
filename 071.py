import requests
 
r = requests.get("http://www.pythonhow.com/data/universe.txt")
text = r.text
count_a = text.count("a")
print(count_a)