from packege import *
from models.Aircraft import Aircraft


def creat_aircraft(path_json):
    aircraft_json = file.read_json(path_json)
    return [Aircraft(**a) for a in aircraft_json]

