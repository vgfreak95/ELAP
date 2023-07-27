"""
Things that must be initialized within things in this file

Must define World Class object for the game with a game name
Create an equal number of items and locations with rules
A win condition
At least 1 Region object

"""

from worlds.AutoWorld import World
from .Options import el_options
from .Items import lookup_item_to_name
from .Locations import location_table

class ELWorld(World):
    """
    Ender Lilies: QUEITES OF THE KNIGHTS: put summary here...?

    """
    game = "Ender Lilies"
    options_definitions = el_options
    topology_present = True

    item_name_to_id = lookup_item_to_name
    location_name_to_id = location_table
