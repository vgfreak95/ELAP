"""
Things that must be initialized within things in this file

Must define World Class object for the game with a game name
Create an equal number of items and locations with rules
A win condition
At least 1 Region object

"""

from worlds.AutoWorld import World
from BaseClasses import Region, ItemClassification as IC
from .Options import el_options
from .Items import ELItem, item_data_table, id_to_item_table, is_progression
from .Locations import location_table, location_data_table, ELLocation
from .Regions import region_data_table

import logging
from typing import List
from worlds.generic.Rules import add_rule, set_rule, forbid_item

class ELWorld(World):
    """
    Ender Lilies: QUEITES OF THE KNIGHTS: put summary here...?

    """
    game = "EnderLilies"
    options_definitions = el_options
    topology_present = True

    # item_name_to_id = {item_name: data.code for item_name, data, in item_data_table.items() if data.code}
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

    def create_items(self) -> None:
        """
        Create the items for the AP World and add them to the item pool
        """
        item_pool: List[ELItem] = []
        logging.info("Creating the items...")

        # Create items for the item pool, eventually might need more logic here
        for name, item in item_data_table.items():
            # logging.info(f"Creating item: {name}")
            # fill progression items first
            item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool
        logging.info("All items should be created")
        print(f"Item Pool items: {self.multiworld.itempool}")

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

            # Currently haven't added the exits to the regions
            # region.add_exits(region_data_table[region_name].connecting_regions)

        print(f"Locations: {self.multiworld.get_locations(1)}")

    def set_rules(self) -> None:

        print("Setting a rule")
        set_rule(self.multiworld.get_location("Abyss_01_GAMEPLAY.BP_Interactable_Item_Tip3", 1), lambda state: state.has("SomeItem", 1))
        print(self.multiworld.get_location("Abyss_01_GAMEPLAY.BP_Interactable_Item_Tip3", 1))

    def get_filler_item_name(self) -> str:
        return "Some filler item (Better luck next time)"

