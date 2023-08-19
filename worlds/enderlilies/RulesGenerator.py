from jinja2 import Environment, FileSystemLoader
from yaml import parse
from data.DataExtractor import nodes_table
import re


# Load the jinja template file
environment = Environment(loader=FileSystemLoader("worlds\\enderlilies\\templates"))
template = environment.get_template("RulesTemplate.pyt")

# Filter the rules
rules_list = []
rule_keys = []

for name, data in nodes_table.items():
    if "WorldTravel" in name or name == "starting_weapon":
        continue
    else:
        rules_list.append(data.get('rules'))
        rule_keys.append(name)
    

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
        else:
            parsed_rule += f"state.has('{token}', player)"

    return parsed_rule

rule_collection = list(map(parse_logic_rule, rules_list))
rule_map = dict(zip(rule_keys, rule_collection))
content = template.render(
    rule_map=rule_map
)

# print(content)
with open("worlds\\enderlilies\\GeneratedRules.py", "w") as file:
    file.writelines(content)

