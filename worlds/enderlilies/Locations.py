from typing import Callable, Dict, NamedTuple, Optional
import re

from BaseClasses import Location, MultiWorld
from .Consts import Regions as region
from .data.DataExtractor import nodes_table, map_location_to_alias




class ELLocation(Location):
    game = "EnderLilies"

class ELLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    rules: str = ""
    content: str = ""
    # can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, ELLocationData] = {}


node_pattern = re.compile(r"[A-Za-z]+\_?\d*\_?\d*\_?", re.IGNORECASE)

for i, (name, info) in enumerate(nodes_table.items()):
    # print(info)

    address = i
    rules = info["rules"] if info.get("rules") else None
    content = info["content"] if info.get("content") else None

    # Remove Travel Volumes and extra content

    current_region = str.join("", node_pattern.search(name).group().split("_"))

    if "WorldTravel" in name:
        location_data = ELLocationData(region=current_region, rules=rules)
        map_code = map_location_to_alias[info.get('content')]
        location_data_table.update({map_code: location_data})
        continue
    # if "WorldTravel" in name or name == "CathedralCloister" or name == "MourningHall":
    #     continue


    location_data_table.update({name: ELLocationData(region=current_region, address=i, rules=rules, content=content)})

# print(len(list(location_data_table.keys())))

# for name, location in location_data_table.items():
#     print(name, location)

location_table: Dict[str, int] = {
    name: data.address for name, data in location_data_table.items() if data.address is not None
}

print(f"Location table: {location_table}")

# print("Length of the location data table: ", len(location_data_table))
# for k, v in location_table.items():
#     print(k, v)
