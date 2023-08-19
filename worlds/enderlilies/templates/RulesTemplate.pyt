from functools import partial

def set_generated_rules(el_world, el_set_rule):
    player = el_world.player
    fn = partial(el_set_rule, el_world)

    # Locations

    {% for rule_name, logic_rule in rule_map.items() -%}
    fn("{{ rule_name }}", {{ logic_rule }})
    {% endfor -%}
