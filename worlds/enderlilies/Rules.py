from worlds.generic.Rules import add_rule, set_rule, forbid_item

def set_rules(self) -> None:

    print("Setting a rule")
    set_rule(self.multiworld.get_location("Abyss01", 1), lambda state: state.has("SomeItem", 1))