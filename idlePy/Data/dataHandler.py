import json

jsonData = open('idleData.json')
jsonArray = json.load(jsonData)
store_list = []

for item in jsonArray:
    character_details = {"name":None, "cash":None}
    character_details['name'] = item['name']
    character_details['cash'] = item['cash']
    store_list.append(character_details)

print(store_list)