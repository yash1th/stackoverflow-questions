import json

input_file = open ('stores-small.json')
json_array = json.load(input_file)
store_details = {"name":None, "city":None}
store_list = []

for item in json_array:
    store_details['name'] = item['name']
    store_details['city'] = item['city']
    store_list.append(store_details)

print(store_list)