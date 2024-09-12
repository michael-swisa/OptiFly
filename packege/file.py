import json
import csv

def read_csv(csv_file_path):
   with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       return list(csv_reader)

def write_csv(csv_file_path, data):
    with open(fr'{csv_file_path}\data_semicolon.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerows(data)

def read_json(path_to_json):
    with open(path_to_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(path_to_json, data):
    with open(path_to_json, 'w') as f:
        json.dump(data, f, indent=4)
