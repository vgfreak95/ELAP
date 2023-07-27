from typing import Dict
from Options import Choice, Option, Toggle


class ShuffleSlots(Toggle):
    display_name = "Shuffle Slots"

class ShuffleBGM(Toggle):
    display_name = "Shuffle Background Music"

class ShuffleEnemies(Toggle):
    display_name = "Shuffle Enemies"

class NewGamePlus(Toggle):
    display_name = "New Game Plus"

class ForceAncientSouls(Toggle):
    display_name = "Ancient Souls on starting spirit"

class MiniBossIncrementsChapter(Toggle):
    display_name = "Sub Spirits Increment Chapter"

class ShuffleUpgrades(Toggle):
    display_name = "Shuffle Upgrades"

el_options: Dict[str, type(Option)] = {
    "shuffle_slots": ShuffleSlots,
    "shuffle_bgm": ShuffleBGM,
    "shuffle_enemeies": ShuffleEnemies,
    "new_game_plus": NewGamePlus,
    "force_ancient_souls": ForceAncientSouls,
    "mini_boss_incrememnts_chapter": MiniBossIncrementsChapter,
    "shuffle_upgrades": ShuffleUpgrades,
}
