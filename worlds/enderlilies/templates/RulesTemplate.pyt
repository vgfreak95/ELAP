from functools import partial


def set_generated_rules(el_world, el_set_rule):
    player = el_world.player
    fn = partial(el_set_rule, el_world)


    # Defined Macros for location access

    {% for name, rule in macro_map.items() -%}
    {{ name }} = {{ rule }}  
    {% endfor %}

    
    # Events (rules for locations)

    {% for name, rule in travel_map.items() -%}
    fn("{{ name }}", {{ rule }})
    {% endfor %}

    # Locations for items

    {% for rule_name, logic_rule in rule_map.items() -%}
    fn("{{ rule_name }}", {{ logic_rule }})
    {% endfor %}
