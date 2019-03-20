import json
from pprint import pprint

with open ("company1.json","r") as file:
    data=json.loads(file.read())

pprint(data)