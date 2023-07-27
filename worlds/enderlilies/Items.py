"""
This file is used to define the items which exist in a given game

It utilizes the DataExtractor module to get the items

This file contains the following items:
    Spirits
    Abilities/Aptitudes
    Relics/Passives
    
"""

from BaseClasses import ItemClassification as IC
import typing
from data.DataExtractor import (
    spirits_table, abilities_table, relics_table
)

class ItemData(typing.NamedTuple):
    classification: IC
    code_name: typing.Optional[str]
    code: typing.Optional[int]


item_table = {}

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
    
    item_table.update(
        {name: ItemData(progression_type, id, i)}
    )


# Handle the abilities
for i, (name, id) in enumerate(abilities_table.items()):

    progression_type: IC
    
    match (name):
        case "ults":
            progression_type = IC.filler
        case _:
            progression_type = IC.progression

    item_table.update(
        {name: ItemData(progression_type, id, i)}
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

    item_table.update(
        {name: ItemData(progression_type, id, i)}
    )


# Individaully lists every item in the game and associates them with an ItemData
# item_table = {
#
#     # Progression Items
#     "silva": ItemData(IC.progression, "Spirit.s5020" , 5020),
#     "sinner": ItemData(IC.progression, "Spirit.s2052", 2052),
#     "djump": ItemData(IC.progression, "Aptitude.double_jump", 0),
#     "dodge": ItemData(IC.progression, "Aptitude.Dodge", 1),
#     "dash": ItemData(IC.progression, "Aptitude.dash", 2),
#     "dash_attack": ItemData(IC.progression, "Aptitude.dash_attack", 3),
#     "slam": ItemData(IC.progression, "Aptitude.pound_attack", 4),
#     "swim": ItemData(IC.progression, "Aptitude.dive", 5),
#     "claw": ItemData(IC.progression, "Aptitude.wallgrab", 6),
#     "hook": ItemData(IC.progression, "Aptitude.hook", 7),
#     "unlock": ItemData(IC.progression, "Aptitude.unlock", 8),
#
#
#     # Filler Items Relics,
#     "Soiled Prayer Beads": ItemData(IC.filler, "Passive.i_passive_maxhpup_LV1", 10),
#     "Royal Aegis Crest": ItemData(IC.filler, "Passive.i_passive_maxhpup_LV2", 11),
#     "Unused Relic 1": ItemData(IC.filler, "Passive.i_passive_maxhpup_LV3", 12),
#     "Broken Music Box": ItemData(IC.filler, "Passive.i_passive_dmgcut_LV1", 13),
#     "Cracked Familiar Stone": ItemData(IC.filler, "Passive.i_passive_dmgcut_LV2", 14),
#     "Snowdrop Bracelet": ItemData(IC.filler, "Passive.i_passive_dmgcut_LV3", 15),
#     "Blighted Appendage": ItemData(IC.filler, "Passive.i_passive_dmgup", 16),
#     "Giant's Ring": ItemData(IC.filler, "Passive.i_passive_dmgup_grounded", 17),
#     "Unused Relic 2": ItemData(IC.filler, "Passive.i_passive_dmgup_grounded_LV2", 18),
#     "Ancient Dragon Claw": ItemData(IC.filler, "Passive.i_passive_dmgup_airborne", 19),
#     "Unused Relic 3": ItemData(IC.filler, "Passive.i_passive_dmgup_airborne_LV2", 20),
#     "Rusted Blue Ornament": ItemData(IC.filler, "Passive.i_passive_dmgup_swimming", 21),
#     "Executioner's Gloves": ItemData(IC.filler, "Passive.i_passive_dmgup_maxhp", 22),
#     "Decayed Crown": ItemData(IC.filler, "Passive.i_passive_stunstamina_damage_up", 23),
#     "Weathered Necklace": ItemData(IC.filler, "Passive.i_passive_regenHP_kill", 24),
#     "Immortal's Crest": ItemData(IC.filler, "Passive.i_passive_regenHP_attack", 25),
#     "Manisa's Ring": ItemData(IC.filler, "Passive.i_passive_spirit_maxcast_count_up_LV1", 26),
#     "Aura's Ring": ItemData(IC.filler, "Passive.i_passive_spirit_maxcast_count_up_LV2", 27),
#     "Unused Relic 4": ItemData(IC.filler, "Passive.i_passive_spirit_maxcast_count_up_LV3", 28),
#     "Kilteus' Ring": ItemData(IC.filler, "Passive.i_passive_recast_time_cut_LV1", 29),
#     "Calivia's Ring": ItemData(IC.filler, "Passive.i_passive_recast_time_cut_LV2", 30),
#     "Unused Relic 5": ItemData(IC.filler, "Passive.i_passive_recast_time_cut_LV3", 31),
#     "White Priestess Statue": ItemData(IC.filler, "Passive.i_passive_heal_count_up_1", 32),
#     "Priestess' Doll": ItemData(IC.filler, "Passive.i_passive_heal_count_up_3", 33),
#     "White Priestess' Earrings": ItemData(IC.filler, "Passive.i_passive_heal_count_up_2", 34),
#     "Holy Spring Water": ItemData(IC.filler, "Passive.i_passive_heal_power_up", 35),
#     "Nymphilia's Ring": ItemData(IC.filler, "Passive.i_passive_shortheal", 36),
#     "Spellbound Anklet": ItemData(IC.filler, "Passive.i_passive_move_speed_up", 37),
#     "Vibrant Plume": ItemData(IC.filler, "Passive.i_passive_jump_height_up", 38),
#     "Ruined Witch's Book": ItemData(IC.filler, "Passive.i_passive_swim_fast", 39),
#     "Bloodstained Ribbon": ItemData(IC.filler, "Passive.i_passive_expup_1", 40),
#     "Blightwreathed Blade": ItemData(IC.filler, "Passive.i_passive_expup_2", 41),
#     "Heretic's Mask": ItemData(IC.filler, "Passive.i_passive_ignore_damage_area", 42),
#     "Unused Relic 6": ItemData(IC.filler, "Passive.i_passive_stamina_up", 43),
#     "Eldred's Ring": ItemData(IC.filler, "Passive.i_passive_mp_restore_up_LV1", 44),
#     "Ricorus' Ring": ItemData(IC.filler, "Passive.i_passive_maxmpup", 45),
#     "Iris' Ring": ItemData(IC.filler, "Passive.i_passive_post_damage_invincibility", 46),
#     "Luminant Aegis Curio": ItemData(IC.filler, "Passive.i_passive_flag_ending_c", 47),
#     "Lost Heirloom": ItemData(IC.filler, "Passive.i_passive_override_skin_level", 48),
#     "Blighted Phantom": ItemData(IC.filler, "Passive.i_passive_override_skin_level_max", 49),
#     "Fretia's Ring": ItemData(IC.filler, "Passive.i_passive_parry", 50),
#
#
#     # Filler Spirits
#     "umbral": ItemData(IC.filler, "Spirit.s5000", 5000),
#     "gerrod": ItemData(IC.filler, "Spirit.s5050", 5050),
#     "julius": ItemData(IC.filler, "Spirit.s5030", 5030),
#     "ulv": ItemData(IC.filler, "Spirit.s5070", 5070),
#     "eleine": ItemData(IC.filler, "Spirit.s5040", 5040),
#     "hoenir": ItemData(IC.filler, "Spirit.s5060", 5060),
#     "faden": ItemData(IC.filler, "Spirit.s5080", 5080),
#     "siegrid": ItemData(IC.filler, "Spirit.s5010", 5010),
#     "youth": ItemData(IC.filler, "Spirit.s2012", 2012),
#     "defender": ItemData(IC.filler, "Spirit.s2002", 2002),
#     "bird": ItemData(IC.filler, "Spirit.s2102", 2102),
#     "dog": ItemData(IC.filler, "Spirit.s2082", 2082),
#     "archer": ItemData(IC.filler, "Spirit.s2022", 2022),
#     "crypt": ItemData(IC.filler, "Spirit.s2162", 2162),
#     "fungal": ItemData(IC.filler, "Spirit.s2122", 2122),
#     "floral": ItemData(IC.filler, "Spirit.s2132", 2132),
#     "sentinel": ItemData(IC.filler, "Spirit.s2192", 2192),
#     "subject": ItemData(IC.filler, "Spirit.s2072", 2072),
#     "executionner": ItemData(IC.filler, "Spirit.s2182", 2182),
#     "champion": ItemData(IC.filler, "Spirit.s2172", 2172),
#     "elder": ItemData(IC.filler, "Spirit.s2112", 2112),
#     "chief": ItemData(IC.filler, "Spirit.s2092", 2092),
#     "aegis": ItemData(IC.filler, "Spirit.s2032", 2032),
#     "fellwyrm": ItemData(IC.filler, "Spirit.s2232", 2232),
#
# }

#lookup_item_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data, in item_table.items() if data.code}

lookup_item_to_name: typing.Dict[str, int] = {
    item_name: data.code for item_name, data, in item_table.items() if data.code is not None
}


