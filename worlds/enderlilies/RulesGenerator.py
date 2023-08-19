from jinja2 import Environment, FileSystemLoader
from data.DataExtractor import nodes_table


environment = Environment(loader=FileSystemLoader("worlds\\enderlilies\\templates"))
template = environment.get_template("RulesTemplate.pyt")

rules_list = list(rule.get("rules") for rule in nodes_table.values())

# (dash + claw) | hook
# lambda state: (state.has(dash) and state.has(claw)) or hook

# index for umbral
rules_list.pop(len(rules_list)-1)

def parse_logic_rule(rule: str) -> str:
    """
    Takes in a rule to create a string verion of the lambda for state
    """

    current_parens = 0

    if rule == None:
        return f"lambda state: True"

    logic_tokens = rule.split(" ")

    # dash, +, claw, |, hook

    # rule: Callable = lambda state: state.has(token)

    # Set an inital rule for location
    current_logic_token = ""
    init_rule: str = f"lambda state: state.has('{logic_tokens[0]}', player)"
    if " " not in rule:
        # print("This might be the issue")
        return init_rule

    # Skip the first logic token
    for token in logic_tokens[1:]:
        # print(token)

        # When logic tokens are found
        if token == "+" or token == "|":
            if token == "+":
                current_logic_token = "and"
            elif token == "|":
                current_logic_token = "or"
        else:
            if "(" in token:
                current_parens += 1
                init_rule += f" {current_logic_token} (state.has('{token[1:]}', player)"
                # dash + (djump | (claw | hook))
                # dash and (state.has(djump) or state.has(claw))
                # state.has(dash) and (state.has(djump) or (state.has(claw) or state.has(hook)))
            elif ")" in token:
                # current_parens -= 1
                init_rule += f" {current_logic_token} state.has('{token[:-1]}', player)" + ")"*current_parens
                current_parens = 0
            else:
                init_rule += f" {current_logic_token} state.has('{token}', player)"
    

    if current_parens == 0:
        return init_rule
    else:
        print("Something went horribly wrong")
        return "There was an error"

# example_rule = "Village04Right + (hook + (LEDGE | claw) | LEDGE + HORIZONTAL | 2LEDGE | LEDGE + claw)"
# print(parse_logic_rule("dash + (djump | (claw | hook))"))
# print(parse_logic_rule(example_rule))
# lambda state: state.has("") and (state.has("") and (state.has("") or state.has(""))) or state.has("") and state.has("") or state.has("") or state.has("") and state.has("")
# for i, rule in enumerate(rules_list):
#     if rule is None:
#         print(f"Previous rule: {rules_list[i-1]}")
#         print(f"Found none at: {rule}")
#     else:
#         print("Correct")


rule_collection = list(map(parse_logic_rule, rules_list))
rule_keys = list(nodes_table.keys())[:-1]
rule_map = dict(zip(rule_keys, rule_collection))
print(parse_logic_rule("dash + (claw | hook)"))
content = template.render(
    rule_map=rule_map
)

print(content)

with open("worlds\\enderlilies\\GeneratedRules.py", "w") as file:
    file.writelines(content)
#


