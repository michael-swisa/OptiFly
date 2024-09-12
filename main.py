from packege import *
from services import *


key = 'a10e75d5c94c635e8496808e1a2918a5'
csv_path = r'files\air_strike_targets.csv'
targets_json = r'models\targets.json'



targets_servic.creat_json_targets(csv_path, targets_json, key)

print(pilots_servic.creat_pilosts(r'files\pilots.json'))