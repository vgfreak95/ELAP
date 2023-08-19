from typing import Callable

from worlds.generic.Rules import add_rule, set_rule, forbid_item, CollectionRule
from BaseClasses import MultiWorld, CollectionState, Location 
from ..AutoWorld import World

from .GeneratedRules import set_generated_rules

import jinja2
from functools import partial


def el_set_rule(el_world: World, location: str, rule):
    player = el_world.player
    # locations = el_world.get_locations(player)
    locations = el_world.multiworld.get_locations(player)

    if locations is None:
        try:
            locations = [el_world.multiworld.get_location(location, player)]
        except KeyError:
            return

    for loc in locations:
        set_rule(loc, rule)


def set_rules(el_world: World):
    set_generated_rules(el_world, el_set_rule)




def set_location_rule_from_template(location: Location, template_logic: str, player: int) -> None:

    logic_tokens = template_logic.split(" ")

    # Set an inital rule for location
    current_logic_token = ""
    init_rule: CollectionRule = lambda state: state.has(logic_tokens[0], player)
    set_rule(location, init_rule)

    # Skip the first logic token
    for token in logic_tokens[1:]:

        # When logic tokens are found
        if not token.isalpha():
            if token == "+":
                current_logic_token = "and"
            elif token == "|":
                current_logic_token = "or"
        else:
            print(f"Adding rule for {token}")
            add_rule(location, lambda state: state.has(token, player), current_logic_token)









def spirit_rule(multiworld: MultiWorld, player: int, spirit: str):
    return lambda state: state.has(spirit, player)

def aptitude_rule(multiworld: MultiWorld, player: int, aptitude: str):
    return lambda state: state.has(aptitude, player)

def relic_rule(multiworld: MultiWorld, player: int, relic: str):
    return lambda state: state.has(relic, player)



