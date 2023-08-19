"""
This file is used to define the items which exist in a given game

It utilizes the DataExtractor module to get the items

This file contains the following items:
    Spirits
    Abilities/Aptitudes
    Relics/Passives
    
"""

from BaseClasses import ItemClassification as IC
from BaseClasses import Item
import typing

from .data.DataExtractor import (
    nodes_table, abilities_table, map_location_to_alias
)


class ELItem(Item):
    game: str = "EnderLilies"

class ELItemData(typing.NamedTuple):
    name: typing.Optional[str]
    code: typing.Optional[int]
    classification: IC



item_data_table = {}


# Silva, Verboten Champion, and Sinner
progressive_spirits = ["Spirit.s2172", "Spirit.s2052", "Spirit.s5020"]

# These will be used as items to replace in the future
tip_indexes = []

for i, (node_name, node_data) in enumerate(nodes_table.items()):

    # Remove Travel Volumes and starting weapon
    if node_name == "starting_weapon":
        continue
        
    # if "WorldTravel" in node_name:
    #     item_data = ELItemData(
    #         classification=IC.filler,
    #         name=node_name,
    #         code=None
    #     )
    #     map_code = map_location_to_alias[node_data.get('content')]
    #     item_data_table.update({map_code: item_data})
    #     continue

    
    if "Tip" in node_name:
        tip_indexes.append(f"{i}_{node_data['content']}")

    # guard clause for any content that's nothing
    if node_data.get('content') == None:
        continue

    item_data = ELItemData(
        classification=IC.filler,
        name=node_data['content'],
        code=i
    )
    # print(f"{i}: {item_data.name}")

    # item_data_table.update({node_data['content']: item_data})
    item_data_table.update({f"{i}_{item_data.name}": item_data})


# Section to add additional items not in nodes
items_to_add = {} # alias, item_name
items_to_add.update(abilities_table)

print(f"Length of data table before: {len(item_data_table)}")
# print(f"Table before: {item_data_table}")


for i, (alias, name) in enumerate(items_to_add.items()):

    # Each item MUST replace a tips content not the tip itself
    replacable_tip_code = item_data_table[tip_indexes[i]].code
    replacable_tip = tip_indexes[i]

    override_item_data = ELItemData(
        classification=IC.progression,
        name=name,
        code=replacable_tip_code
    )

    # print(name)

    del item_data_table[replacable_tip]
    # del item_data_table[tip_indexes[i+12]]
    item_data_table.update({name: override_item_data})



print(item_data_table)



# print(item_data_table.get(replacable_tip))


print(f"Length of data table after: {len(item_data_table)}")
# print(f"Table before: {item_data_table.keys()}")

"""
Example Item Table
    heal1: IC.progression, code_name='heal1', code=10
"""



id_to_item_table: typing.Dict[int, str] = {data.code: item_name for item_name, data, in item_data_table.items() if data.code is not None}

def is_progression(item: str):
    if item_data_table[item].classification == IC.progression:
        return True
    return False
