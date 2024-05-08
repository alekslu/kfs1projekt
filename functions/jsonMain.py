# Importing required modules 
import json

#jsonFile = 'data/data.json'
jsonFile = 'data/data_bigger.json'

with open(jsonFile, 'r') as inside:
    json_data = json.load(inside)
    
json_str = json.dumps(json_data, indent = 3)

checkbox_list=[]

def print_no_duplicate_keys(json_data, breadcrumbs=""):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            new_breadcrumbs = key if not breadcrumbs else f"{breadcrumbs}.{key}"
            print(new_breadcrumbs)
            print_no_duplicate_keys(value,new_breadcrumbs)
            if new_breadcrumbs not in checkbox_list:
                checkbox_list.append(new_breadcrumbs)
    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            new_breadcrumbs = f"{breadcrumbs}"
            if new_breadcrumbs not in checkbox_list and index < 1:
                print_no_duplicate_keys(item, new_breadcrumbs)
                checkbox_list.append(new_breadcrumbs)

print_no_duplicate_keys(json_data)
print(checkbox_list)

def get_nested_values(data, keys):
    key_list = keys.split('.')
    if len(key_list) == 1:
        return find_values(data, key_list[0])
    else:
        return find_nested_values(data, key_list)


def find_values(data, key):
    if isinstance(data, dict):
        if key in data:
            return data[key]
    elif isinstance(data, list):
        result = []
        for item in data:
            if isinstance(item, dict) and key in item:
                result.append(item[key])
        return result if result else None
    return None


def find_nested_values(data, key_list):
    key = key_list[0]
    if isinstance(data, dict):
        if key in data:
            nested_data = data[key]
            if len(key_list) > 1:
                return get_nested_values(nested_data, '.'.join(key_list[1:]))
            else:
                return nested_data
    elif isinstance(data, list):
        result = []
        for item in data:
            nested_data = find_nested_values(item, key_list)
            if nested_data is not None:
                if isinstance(nested_data, list):
                    result.extend(nested_data)
                else:
                    result.append(nested_data)
        return result if result else None
    return None