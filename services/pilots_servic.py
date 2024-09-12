from packege import *
from models.Pilot import Pilot





def creat_pilosts(path_json):
    pilost_json = file.read_json(path_json)
    pilots_list = []
    return [Pilot(**p) for p in pilost_json]





