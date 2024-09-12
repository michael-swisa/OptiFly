import json
import csv

def read_csv(csv_file_path):
   with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       return list(csv_reader)

def read_json(path_to_json):
    with open(path_to_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(path_to_json, data):
    with open(path_to_json, 'w') as f:
        json.dump(data, f, indent=4)
