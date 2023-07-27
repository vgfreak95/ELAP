from typing import Dict, List, NamedTuple
from .Consts import Regions as region

class ELRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table = {
    region.ABYSS: ELRegionData(),
    region.CASTLE: ELRegionData(),
    region.CAVE: ELRegionData(),
    region.CHURCH: ELRegionData(),
    region.FOREST: ELRegionData(),
    region.FORT: ELRegionData(),
    region.OUBLIETTE: ELRegionData(),
    region.SWAMP: ELRegionData(),
    region.VILLAGE: ELRegionData(),
}
