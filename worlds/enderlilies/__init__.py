"""
Things that must be initialized within things in this file

Must define World Class object for the game with a game name
Create an equal number of items and locations with rules
A win condition
At least 1 Region object

"""

from worlds.AutoWorld import World
from BaseClasses import Region, ItemClassification as IC
from worlds.ladx.LADXR.logic import location
from .Options import el_options
from .Items import ELItem, item_data_table, id_to_item_table, is_progression
from .Locations import location_table, location_data_table, ELLocation
from .Regions import region_data_table
from.data.DataExtractor import (
    region_rooms, spirits_table, abilities_table, macros_table, relics_table 
)


from .Rules import (
    relic_rule, aptitude_rule, spirit_rule, set_location_rule_from_template, set_rules
)

import logging
from typing import List
from worlds.generic.Rules import (
    CollectionRule, add_rule, set_rule, forbid_item, 
)

class ELWorld(World):
    """
    Ender Lilies: QUIETUS OF THE KNIGHTS: put summary here...?

    """
    game = "EnderLilies"
    options_definitions = el_options
    topology_present = True
    item_name_to_id = {item_name: data.code for item_name, data in item_data_table.items() if data.code is not None}
    location_name_to_id = location_table

    def create_item(self, name: str) -> ELItem:
        """
        Creates an item by using the name and is possible because of
        the item data table lookup

        :param name: The name of the item to create, must match the item data table
        """

        # logging.info(f"Creating Item: {name}")
        return ELItem(
            name=name,
            code=item_data_table[name].code,
            classification=item_data_table[name].classification,
            player=self.player
        )

    def create_event(self, name:str) -> ELItem:
        """
        Creates an event item that isn't used in the game but only used in the logic
        """

        return ELItem(
            name=name,
            classification=IC.filler,
            code=None,
            player=self.player
        )

    def create_items(self) -> None:
        """
        Create the items for the AP World and add them to the item pool
        """
        item_pool: List[ELItem] = []
        logging.info("Creating the items...")

        # Create items for the item pool, eventually might need more logic here
        for name, item in item_data_table.items():
            item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool
        logging.info("All items should be created")
        # print(f"Item Pool items: {self.multiworld.itempool}")

    def create_regions(self) -> None:
        """
        Create the regions (rooms) for the world and add locations to each room
        in the world
        """
        logging.info("Creating the regions...")

        # Add the menu region
        menu_region = Region("Menu", self.player, self.multiworld) 
        self.multiworld.regions.append(menu_region)

        # Create the regions and add them to the multiworld
        for region_name in region_data_table.keys():
            # logging.info(f"Created region {region_name}")
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Add the locations to each region that gets created
        for region_name, region_data in region_data_table.items():
            locations = {}
            region: Region = self.multiworld.get_region(region_name, self.player)
            for location_name, location_data in location_data_table.items():
                if location_data.region == region.name:
                    locations.update({location_name: location_data.address})

            # Locations can be empty if World Travel Volume exists but item location doesn't
            if len(locations) != 0:
                region.add_locations(locations, ELLocation)

        # Add exits for the region room
        for room_name in region_rooms:
            region: Region = self.multiworld.get_region(room_name, self.player)
            region.add_exits(region_data_table[room_name].connecting_regions)

    def set_rules(self) -> None:
        set_rules(self)

    def get_filler_item_name(self) -> str:
        return "Some filler item (Better luck next time)"

