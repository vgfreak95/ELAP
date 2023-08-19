from jinja2 import Environment, FileSystemLoader
from yaml import parse
from data.DataExtractor import (
    nodes_table, macros_table, abilities_table, relics_table, map_alias_to_location,
    nodes_alias_table, map_location_to_alias
)
import re


# Load the jinja template file
environment = Environment(loader=FileSystemLoader("worlds\\enderlilies\\templates"))
template = environment.get_template("RulesTemplate.pyt")

# Filter the rules
rules_list = []
rule_keys = []

location_rules = []
location_rule_keys = []

# Where the items location rules are defined
for name, data in nodes_table.items():
    if "WorldTravel" in name or name == "starting_weapon":
        continue

    if name == "starting_weapon":
        continue
    else:
        rules_list.append(data.get('rules'))
        rule_keys.append(name)
    

for name, data in nodes_table.items():
    if "WorldTravel" in name:
        map_code = data['content']
        aliased_volume = map_location_to_alias[map_code]
        location_rule_keys.append(aliased_volume)
        location_rules.append(data.get('rules'))



renamed_macros = {    
    "3LEDGE": "THREE_LEDGE",
    "2LEDGE": "TWO_LEDGE",
    "LEDGE": "LEDGE",
    "2HORIZONTAL": "TWO_HORIZONTAL",
    "HORIZONTAL": "HORIZONTAL",
    "FULLSILVA": "FULLSILVA",
    "CHARGE": "CHARGE",
    "3HEAL": "THREE_HEAL"
}

def parse_logic_rule(rule: str) -> str:
    """
    Takes in a rule to create a string verion of the lambda for state
    """

    if rule == None:
        return f"lambda state: True"
    
    # New code using regex
    logic_pattern = r"\b\w+\b|\(|\)|\||\+"
    
    # Tokenization
    logic_tokens = re.findall(logic_pattern, rule)

    single_rule = len(logic_tokens) == 1
    parsed_rule = "lambda state: "


    if single_rule: 
        if logic_tokens[0] in nodes_alias_table.keys():
            return parsed_rule + f"state.has('{nodes_alias_table[logic_tokens[0]]}', player)"
        if logic_tokens[0] in map_alias_to_location.keys():
            return parsed_rule + f"state.has('{logic_tokens[0]}', player)"
        elif logic_tokens[0] in abilities_table.keys():
            return parsed_rule + f"state.has('{abilities_table[logic_tokens[0]]}', player)"
        elif logic_tokens[0] in relics_table.keys():
            return parsed_rule + f"state.has('{relics_table[logic_tokens[0]]}', player)"
        elif logic_tokens[0] in macros_table.keys():
            return parsed_rule + f"state.has({renamed_macros[logic_tokens[0]]}, player)"
        else:
            return f"lambda state: state.has('{logic_tokens[0]}', player)"
    

    for token in logic_tokens:
        if token == "+":
            parsed_rule += " and "
        elif token == "|":
            parsed_rule += " or "
        elif token == "(":
            parsed_rule += "("
        elif token == ")":
            parsed_rule += ")"
        elif token in nodes_alias_table.keys():
            parsed_rule += f"state.has('{nodes_alias_table[token]}', player)"
        elif token in map_alias_to_location.keys():
            # print(token)
            parsed_rule += f"state.has('{token}', player)"
        elif token in abilities_table.keys():
            parsed_rule += f"state.has('{abilities_table[token]}', player)"
        elif token in relics_table.keys():
            parsed_rule += f"state.has('{relics_table[token]}', player)"
        elif token in macros_table.keys():
            parsed_rule += f"state.has({renamed_macros[token]}, player)"
        else:
            # if "World" in token:
                # print(f"Found world: {token}")
            parsed_rule += f"state.has('{token}', player)"

    return parsed_rule

# print(region_connectors_lookup.keys())

rule_collection = list(map(parse_logic_rule, rules_list))
rule_map = dict(zip(rule_keys, rule_collection))

macro_rules = list(map(parse_logic_rule, list(macros_table.values())))
macro_names = list(renamed_macros.values())
macro_map = dict(zip(macro_names, macro_rules))

location_collection = list(map(parse_logic_rule, location_rules))
travel_map = dict(zip(location_rule_keys, location_collection))

content = template.render(
    rule_map=rule_map,
    macro_map=macro_map,
    travel_map=travel_map
)

# print(content)
with open("worlds\\enderlilies\\GeneratedRules.py", "w") as file:
    file.writelines(content)

