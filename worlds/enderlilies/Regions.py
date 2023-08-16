from typing import Dict, List, NamedTuple
from .data.DataExtractor import region_rooms, room_exits, region_connectors_lookup, map_alias_to_location

class ELRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table = {}

for region_name in region_rooms:
    connectors = room_exits[region_name]
    region_data_table.update({region_name: ELRegionData(connectors)})
