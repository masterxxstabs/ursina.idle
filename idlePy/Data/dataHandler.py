import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_json_array(json_data, key):
    return json_data.get(key, [])

def write_json_array(json_data, key, array):
    json_data[key] = array