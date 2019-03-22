import json

with open ("company1.json","r+") as file:
    data=json.loads(file.read())
    data["employees"].append(dict(firstName="Albert",lastName="Bert"))
    file.seek(0)
    json.dump(data, file, indent=4, sort_keys=True)
    file.truncate()