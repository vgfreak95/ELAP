from typing import Dict, List, NamedTuple
from .Consts import Regions as region

from .data.DataExtractor import region_rooms

class ELRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table = {}
for region_name in region_rooms:
    region_data_table.update({region_name: ELRegionData("Abyss01")})

print(region_data_table)



