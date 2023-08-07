import json

json_data = ""

json_path = "worlds\\enderlilies\\data\\el.json"

with open(json_path, "r") as json_file:
    for line in json_file.readlines():
        json_data += line

ds_data = json.loads(json_data)

alias = ds_data["items_alias"]

spirits_table = alias["spirits"]
abilities_table = alias["abilities"]
relics_table = alias["relics"]

macros_table = ds_data["macros"]

extra_items_list = ds_data["extra_items"]

locations_table = ds_data["locations"]

nodes_alias_table = ds_data["nodes_alias"]

nodes_table = ds_data["nodes"]