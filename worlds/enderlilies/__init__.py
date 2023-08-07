"""
Things that must be initialized within things in this file

Must define World Class object for the game with a game name
Create an equal number of items and locations with rules
A win condition
At least 1 Region object

"""

from worlds.AutoWorld import World
from BaseClasses import Region
from .Options import el_options
from .Items import ELItem, item_data_table, id_to_item_table, is_progression
from .Locations import location_table, location_data_table, ELLocation
from .Regions import region_data_table

from typing import List

class ELWorld(World):
    """
    Ender Lilies: QUEITES OF THE KNIGHTS: put summary here...?

    """
    game = "EnderLilies"
    options_definitions = el_options
    topology_present = True




    item_name_to_id = {item_name: data.code for item_name, data, in item_data_table.items() if data.code}
    item_id_to_name = id_to_item_table
    location_name_to_id = location_table

    def create_item(self, name: str) -> ELItem:
        print(f"Creating Item: {name}")
        return ELItem(
            name=name,
            code=item_data_table[name].code,
            classification=item_data_table[name].classification,
            player=self.player
        )

    def create_items(self) -> None:
        item_pool: List[ELItem] = []

        # Create items for the item pool, eventually might need more logic here
        for name, item in item_data_table.items():
            item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:

        # Create the regions and add them to the multiworld
        for name in region_data_table.keys():
            region = Region(name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create the location and add them to the multiworld
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                # if location_data.region == region_name
            }, ELLocation)

            # Currently haven't added the exists to the regions
            region.add_exits(region_data_table[region_name].connecting_regions)


    def get_filler_item_name(self) -> str:
        return "Some filler item (Better luck next time)"

