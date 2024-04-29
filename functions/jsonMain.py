# Importing required modules 
import json

checkbox_list = []

jsonFile = 'data/data.json'
#jsonFile = 'data/data_bigger.json'

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
