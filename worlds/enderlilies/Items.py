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
    spirits_table, abilities_table, relics_table
)


class ELItem(Item):
    game: str = "EnderLilies"

class ELItemData(typing.NamedTuple):
    name: typing.Optional[str]
    code: typing.Optional[int]
    classification: IC


item_data_table = {}

# Handle the spirits
for i, (name, id) in enumerate(spirits_table.items()):

    progression_type: IC

    # exceptions because they are progression
    match (name):
        case "silva":
            progression_type = IC.progression
        case "sinner":
            progression_type = IC.progression
        case _:
            progression_type = IC.filler

    item_data_table.update(
        {
            name: ELItemData(
                classification=progression_type,
                name=name,
                code=i,
            )
        }
    )

# Handle the abilities
for i, (name, id) in enumerate(abilities_table.items()):

    progression_type: IC

    match (name):
        case "ults":
            progression_type = IC.filler
        case _:
            progression_type = IC.progression

    item_data_table.update(
        {
            name: ELItemData(
                classification=progression_type,
                name=name,
                code=i,
            )
        }
    )

# Handle the relics
for i, (name, id) in enumerate(relics_table.items()):

    progression_type: IC

    match (name):
        case "mask":
            progression_type = IC.progression
        case "heal1":
            progression_type = IC.progression
        case "heal2":
            progression_type = IC.progression
        case "heal3":
            progression_type = IC.progression
        case _:
            progression_type = IC.filler

    item_data_table.update(
        {
            name: ELItemData(
                classification=progression_type,
                name=name,
                code=i,
            )
        }
    )

"""
Example Item Table
    heal1: IC.progression, code_name='heal1', code=10
"""



id_to_item_table: typing.Dict[int, str] = {data.code: item_name for item_name, data, in item_data_table.items() if data.code}


def is_progression(item: str):
    if item_data_table[item].classification == IC.progression:
        return True
    return False
