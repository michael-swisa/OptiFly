import csv
import  requests
from  packege import file, request

key = 'a10e75d5c94c635e8496808e1a2918a5'
csv_path = r'files\air_strike_targets.csv'
targets_json = r'models\targets.json'

# Geographical_location = requests.get(urlGeographical_location)


def creat_json_targets(path_csv, path_json):
    csv_data = file.read_csv(path_csv)
    targets_list = []
    for row in csv_data[1:]:
        cuantry = row[0]
        location = requests.get_location(cuantry, key)
        new_targets = {'City':row[0], 'Priority':row[1], 'lat': location[0]['lat'], 'lon': location[0]['lon'] }
        targets_list.append(new_targets)

    file.write_json(path_json, targets_list)
    return


creat_json_targets(csv_path, targets_json)
