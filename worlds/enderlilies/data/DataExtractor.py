import json
import re

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

map_alias_to_location = ds_data["locations"]

map_location_to_alias = {}

# We need this since generated content should be hashable both ways
for key, value in map_location_to_alias.items():
    map_location_to_alias.update({value: key})

region_rooms = []
# Region = Room and need a list of rooms

pattern = re.compile(r"[A-Za-z]+[0-9]+", re.IGNORECASE)

for name in map_alias_to_location.keys():
    region_room = pattern.match(name).group()

    # quick way to remove duplicates
    if region_room not in region_rooms:
        region_rooms.append(region_room)


nodes_alias_table = ds_data["nodes_alias"]

nodes_table = ds_data["nodes"]
