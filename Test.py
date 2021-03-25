import json
dir = 'Json_Input'
jsonCompare = ['velkoz']
dataset = []
for file in jsonCompare :
    path = f"{dir}/{file}.json"
    with open(path) as json_file:
        data = json.load(json_file)
        dataset.append([x for x in data.keys() if "VelkozQ" in x])

for data in dataset :
    print(str(data))




