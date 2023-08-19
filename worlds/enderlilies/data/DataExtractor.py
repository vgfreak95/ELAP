import json
import re

json_data = ""

json_path = "worlds\\enderlilies\\data\\el.json"

with open(json_path, "r") as json_file:
    for line in json_file.readlines():
        json_data += line

ds_data = json.loads(json_data)

alias = ds_data["items_alias"]
spirits_table = alias["spirits"]
abilities_table = alias["abilities"]
relics_table = alias["relics"]
macros_table = ds_data["macros"]
extra_items_list = ds_data["extra_items"]
map_alias_to_location = ds_data["locations"]

# Leaving line breaks because easier vim navigation
region_connectors_lookup = {

    'Abyss01Bottom': 'Abyss02',
    'Abyss01Top': 'Swamp18',
    'Abyss02Right': 'Abyss03',
    'Abyss02Top': 'Abyss01',
    'Abyss03Left': 'Abyss02',
    'Abyss04Bottom': 'Abyss05',
    'Abyss04Top': 'Swamp12',
    'Abyss05Top': 'Abyss04',

    'Castle01Left': 'Village11',
    'Castle01Right1': 'Castle02',
    'Castle01Right2': 'Castle02',
    'Castle01Top': 'Castle10',
    'Castle02Bottom': 'Castle04',
    'Castle02Left1': 'Castle01',
    'Castle02Left2': 'Castle01',
    'Castle02Top': 'Castle05',
    'Castle03Bottom': 'Castle05',
    'Castle03Top1': 'Castle11',
    'Castle03Top2': 'Castle11',
    'Castle04Top': 'Castle02',
    'Castle05Bottom': 'Castle02',
    'Castle05Left': 'Castle08',
    'Castle05Right': 'Castle06',
    'Castle05Top': 'Castle03',
    'Castle06Left': 'Castle05',
    'Castle06Right': 'Castle07',
    'Castle06Top': 'Castle12',
    'Castle07Left': 'Castle06',
    'Castle07Right': 'Fort01',
    'Castle08Right': 'Castle05',
    'Castle08Top': 'Castle09',
    'Castle09Bottom': 'Castle08',
    'Castle09Left': 'Castle10',
    'Castle09Right': 'Castle11',
    'Castle10Bottom': 'Castle01',
    'Castle10Right': 'Castle09',
    'Castle11Bottom1': 'Castle03',
    'Castle11Bottom2': 'Castle03',
    'Castle11Left': 'Castle09',
    'Castle11Right': 'Castle12',
    'Castle11Top': 'Castle13',
    'Castle12Bottom': 'Castle06',
    'Castle12Left': 'Castle11',
    'Castle12Right': 'Castle21',
    'Castle13Bottom': 'Castle11',
    'Castle13Left': 'Castle17',
    'Castle13Right': 'Castle14',
    'Castle14Left': 'Castle13',
    'Castle14Top': 'Castle15',
    'Castle15Bottom': 'Castle14',
    'Castle15Left': 'Castle16',
    'Castle16Right': 'Castle15',
    'Castle16Bottom': 'Castle18',
    'Castle17Right': 'Castle13',
    'Castle17Top': 'Castle18',
    'Castle18Bottom': 'Castle17',
    'Castle18Right': 'Castle19',
    'Castle18Top': 'Castle16',
    'Castle19Left': 'Castle18',
    'Castle19Right': 'Castle20',
    'Castle20Left': 'Castle19',
    'Castle21Left': 'Castle12',

    'Cave01Bottom': 'Cave02',
    'Cave01Left': 'Village12',
    'Cave02Bottom': 'Cave07',
    'Cave02Right': 'Cave05',
    'Cave02Top': 'Cave01',
    'Cave03Left': 'Cave07',
    'Cave03Right': 'Cave08',
    'Cave03Top': 'Cave06',
    'Cave04Bottom': 'Cave05',
    'Cave04Left': 'Cave12',
    'Cave04Right': 'Cave16',
    'Cave05Bottom': 'Cave06',
    'Cave05Left': 'Cave02',
    'Cave05Right': 'Cave10',
    'Cave05Top': 'Cave04',
    'Cave06Bottom': 'Cave03',
    'Cave06Top': 'Cave05',
    'Cave07Right': 'Cave03',
    'Cave07Top': 'Cave02',
    'Cave08Bottom': 'Cave17',
    'Cave08Left': 'Cave03',
    'Cave08Right': 'Cave11',
    'Cave08Top': 'Cave09',
    'Cave09Bottom': 'Cave08',
    'Cave09Right': 'Cave21',
    'Cave09Top': 'Cave10',
    'Cave10Bottom': 'Cave09',
    'Cave10Left': 'Cave05',
    'Cave10Right': 'Cave23',
    'Cave10Top': 'Cave16',
    'Cave11Left': 'Cave08',
    'Cave11Right1': 'Cave18',
    'Cave11Right2': 'Cave18',
    'Cave11Top': 'Cave13',
    'Cave12Right': 'Cave04',
    'Cave13Bottom': 'Cave11',
    'Cave13Left': 'Cave23',
    'Cave13Right': 'Cave20',
    'Cave13Top': 'Cave14',
    'Cave14Bottom': 'Cave13',
    'Cave14Left': 'Cave15',
    'Cave14Right': 'Cave22',
    'Cave15Left': 'Cave16',
    'Cave15Right': 'Cave14',
    'Cave16Bottom': 'Cave10',
    'Cave16Left': 'Cave04',
    'Cave16Right': 'Cave15',
    'Cave17Top': 'Cave08',
    'Cave18Left1': 'Cave11',
    'Cave18Left2': 'Cave11',
    'Cave19Left': 'Cave21',
    'Cave19Top': 'Cave20',
    'Cave20Bottom': 'Cave19',
    'Cave20Left': 'Cave13',
    'Cave20Top': 'Cave22',
    'Cave21Left': 'Cave09',
    'Cave21Right': 'Cave19',
    'Cave22Bottom': 'Cave20',
    'Cave22Left': 'Cave14',
    'Cave22Right': 'Fort02',
    'Cave23Left': 'Cave10',
    'Cave23Right': 'Cave13',

    'Church01Bottom': 'Church02',
    'Church01Left': 'Church12',
    'Church01Top': 'Church09',
    'Church02Right': 'Church10',
    'Church02Top': 'Church01',
    'Church03Left': 'Church05',
    'Church03Right': 'Church04',
    'Church04Left': 'Church03',
    'Church04Right': 'Church06',
    'Church05Bottom': 'Church11',
    'Church05Right': 'Church03',
    'Church05Top': 'Church09',
    'Church06Left': 'Church04',
    'Church06Right': 'Church07',
    'Church07Left': 'Church06',
    'Church07Right': 'Church08',
    'Church08Bottom': 'Forest01',
    'Church08Left': 'Church07',
    'Church08Top': 'Village01',
    'Church09Bottom': 'Church01',
    'Church09Top': 'Church14',
    'Church10Left': 'Church02',
    'Church10Right': 'Church11',
    'Church11Left': 'Church10',
    'Church11Top': 'Church05',
    'Church12Bottom': 'Church13',
    'Church12Right': 'Church01',
    'Church13Top': 'Church12',
    'Church14Bottom': 'Church09',

    'Forest01Right': 'Forest02',
    'Forest01Top': 'Church08',
    'Forest02Left': 'Forest01',
    'Forest02Right1': 'Forest04',
    'Forest02Right2': 'Forest03',
    'Forest03Left': 'Forest02',
    'Forest03Right': 'Forest05',
    'Forest04Left': 'Forest02',
    'Forest04Right': 'Forest05',
    'Forest05Left': 'Forest04',
    'Forest05Right': 'Forest07',
    'Forest05Top': 'Forest04',
    'Forest06Bottom': 'Forest07',
    'Forest07Bottom': 'Forest08',
    'Forest07Left': 'Forest05',
    'Forest07Right': 'Oubliette01',
    'Forest07Top': 'Forest06',
    'Forest08Right': 'Forest10',
    'Forest08Top': 'Forest07',
    'Forest09Left': 'Swamp2',
    'Forest09Top': 'Forest10',
    'Forest10Bottom1': 'Forest09',
    'Forest10Bottom2': 'Forest11',
    'Forest10Left': 'Forest08',
    'Forest10Right': 'Forest12',
    'Forest11Right': 'Forest14',
    'Forest11Top': 'Forest10',
    'Forest12Bottom': 'Forest13',
    'Forest12Left': 'Forest10',
    'Forest12Right': 'Forest17',
    'Forest13Bottom': 'Forest14',
    'Forest13Right': 'Forest16',
    'Forest13Top': 'Forest12',
    'Forest14Bottom': 'Forest15',
    'Forest14Left': 'Forest11',
    'Forest14Top': 'Forest13',
    'Forest15Top': 'Forest14',
    'Forest16Left': 'Forest13',
    'Forest17Left': 'Forest12',

    'Fort01Left1': 'Castle07',
    'Fort01Left2': 'Village15',
    'Fort01Right': 'Fort03',
    'Fort02Left': 'Cave22',
    'Fort02Right': 'Fort03',
    'Fort03Left1': 'Fort01',
    'Fort03Left2': 'Fort02',
    'Fort03Right': 'Fort04',
    'Fort03Top': 'Fort05',
    'Fort04Left': 'Fort03',
    'Fort04Top': 'Fort05',
    'Fort05Bottom1': 'Fort03',
    'Fort05Bottom2': 'Fort04',
    'Fort05Right': 'Fort06',
    'Fort05Top': 'Fort15',
    'Fort06Bottom': 'Fort10',
    'Fort06Left': 'Fort05',
    'Fort06Right': 'Fort07',
    'Fort07Bottom1': 'Fort09',
    'Fort07Bottom2': 'Fort09',
    'Fort07Left': 'Fort06',
    'Fort07Right': 'Fort08',
    'Fort07Top': 'Fort11',
    'Fort08Left': 'Fort07',
    'Fort09Left': 'Fort10',
    'Fort09Right': 'Outside03',
    'Fort09Top1': 'Fort07',
    'Fort09Top2': 'Fort07',
    'Fort10Right': 'Fort09',
    'Fort10Top': 'Fort06',
    'Fort11Bottom': 'Fort07',
    'Fort11Left': 'Fort12',
    'Fort11Top1': 'Fort13',
    'Fort11Top2': 'Fort13',
    'Fort12Left': 'Fort16',
    'Fort12Right': 'Fort11',
    'Fort12Top': 'Fort14',
    'Fort13Bottom1': 'Fort11',
    'Fort13Bottom2': 'Fort11',
    'Fort13Left': 'Fort14',
    'Fort13Top': 'Fort19',
    'Fort14Bottom': 'Fort12',
    'Fort14Left': 'Fort15',
    'Fort14Right': 'Fort13',
    'Fort15Bottom': 'Fort05',
    'Fort15Right1': 'Fort16',
    'Fort15Right2': 'Fort16',
    'Fort15Right3': 'Fort14',
    'Fort15Top': 'Fort17',
    'Fort16Left1': 'Fort15',
    'Fort16Left2': 'Fort15',
    'Fort16Right': 'Fort12',
    'Fort16Top': 'Fort18',
    'Fort17Bottom': 'Fort15',
    'Fort17Right': 'Fort18',
    'Fort18Bottom': 'Fort16',
    'Fort18Left': 'Fort17',
    'Fort18Right': 'Fort19',
    'Fort19Bottom': 'Fort13',
    'Fort19Left': 'Fort18',
    'Fort19Top': 'Fort20',
    'Fort20Bottom': 'Fort19',
    'Fort20Top': 'Fort21',
    'Fort21Bottom': 'Fort20',

    'Oubliette01Left': 'Forest07',
    'Oubliette01Right': 'Oubliette02',
    'Oubliette02Left': 'Oubliette01',
    'Oubliette02Right1': 'Oubliette05',
    'Oubliette02Right2': 'Oubliette04',
    'Oubliette03Left': 'Oubliette04',
    'Oubliette03Right': 'Oubliette10',
    'Oubliette03Top': 'Oubliette05',
    'Oubliette04Left': 'Oubliette02',
    'Oubliette04Right': 'Oubliette03',
    'Oubliette051Bottom': 'Oubliette05',
    'Oubliette052Bottom1': 'Oubliette05',
    'Oubliette052Bottom2': 'Oubliette05',
    'Oubliette053Top': 'Oubliette05',
    'Oubliette05Bottom1': 'Oubliette071',
    'Oubliette05Bottom2': 'Oubliette053',
    'Oubliette05Bottom3': 'Oubliette03',
    'Oubliette05Left': 'Oubliette02',
    'Oubliette05Right': 'Oubliette06',
    'Oubliette05Top1': 'Oubliette051',
    'Oubliette05Top2': 'Oubliette052',
    'Oubliette05Top3': 'Oubliette052',
    'Oubliette05Top4': 'Oubliette072',
    'Oubliette061Left': 'Oubliette07',
    'Oubliette062Bottom2': 'Oubliette07',
    'Oubliette063Left1': 'Oubliette07',
    'Oubliette064Top': 'Oubliette07',
    'Oubliette06Bottom': 'Oubliette10',
    'Oubliette06Left': 'Oubliette05',
    'Oubliette06Right': 'Oubliette07',
    'Oubliette071Top': 'Oubliette05',
    'Oubliette072Bottom': 'Oubliette05',
    'Oubliette07Bottom1': 'Oubliette09',
    'Oubliette07Bottom2': 'Oubliette062',
    'Oubliette07Left1': 'Oubliette063',
    'Oubliette07Left2': 'Oubliette06',
    'Oubliette07Right1': 'Oubliette061',
    'Oubliette07Right2': 'Oubliette13',
    'Oubliette07Top': 'Oubliette064',
    'Oubliette08Left': 'Oubliette09',
    'Oubliette08Right': 'Oubliette11',
    'Oubliette08Top': 'Oubliette13',
    'Oubliette09Left': 'Oubliette10',
    'Oubliette09Right': 'Oubliette08',
    'Oubliette09Top': 'Oubliette07',
    'Oubliette10Left1': 'Oubliette03',
    'Oubliette10Left2': 'Oubliette17',
    'Oubliette10Right': 'Oubliette09',
    'Oubliette10Top': 'Oubliette06',
    'Oubliette11Bottom': 'Oubliette132',
    'Oubliette11Left1': 'Oubliette13',
    'Oubliette11Left2': 'Oubliette08',
    'Oubliette11Right1': 'Oubliette12',
    'Oubliette11Right2': 'Oubliette14',
    'Oubliette11Top': 'Oubliette131',
    'Oubliette12Left': 'Oubliette11',
    'Oubliette131Bottom': 'Oubliette11',
    'Oubliette132Top': 'Oubliette11',
    'Oubliette13Bottom': 'Oubliette08',
    'Oubliette13Left': 'Oubliette07',
    'Oubliette13Right': 'Oubliette11',
    'Oubliette14Left': 'Oubliette11',
    'Oubliette14Right': 'Oubliette15',
    'Oubliette15Left': 'Oubliette14',
    'Oubliette15Right': 'Oubliette16',
    'Oubliette16Left': 'Oubliette15',
    'Oubliette16Right': 'Outside01',
    'Oubliette17Bottom': 'Swamp06',
    'Oubliette17Right': 'Oubliette10',
    'Outside01Left1': 'Outside03',
    'Outside01Left2': 'Oubliette16',
    'Outside01Right': 'Outside02',
    'Outside02Left': 'Outside01',
    'Outside03Right': 'Outside01',
    'Outside03Top': 'Fort09',

    'Swamp1Bottom': 'Swamp3',
    'Swamp1Left': 'Swamp2',
    'Swamp2Right': 'Swamp1',
    'Swamp2Top': 'Forest09',
    'Swamp3Bottom': 'Swamp07',
    'Swamp3Left': 'Swamp09',
    'Swamp3Right': 'Swamp04',
    'Swamp3Top': 'Swamp1',
    'Swamp04Bottom': 'Swamp05',
    'Swamp04Left': 'Swamp3',
    'Swamp05Bottom': 'Swamp07',
    'Swamp05Left': 'Swamp09',
    'Swamp05Right': 'Swamp06',
    'Swamp05Top': 'Swamp04',
    'Swamp06Left': 'Swamp05',
    'Swamp06Top': 'Oubliette17',
    'Swamp07Bottom': 'Swamp16',
    'Swamp07Left': 'Swamp08',
    'Swamp07Right': 'Swamp05',
    'Swamp07Top': 'Swamp3',
    'Swamp08Right1': 'Swamp07',
    'Swamp08Right2': 'Swamp15',
    'Swamp08Top': 'Swamp14',
    'Swamp09Bottom1': 'Swamp13',
    'Swamp09Bottom2': 'Swamp13',
    'Swamp09Right1': 'Swamp3',
    'Swamp09Right2': 'Swamp05',
    'Swamp10Right': 'Swamp13',
    'Swamp11Bottom': 'Swamp15',
    'Swamp11Left': 'Swamp14',
    'Swamp12Bottom': 'Abyss04',
    'Swamp12Left': 'Swamp15',
    'Swamp12TP': 'Abyss05',
    'Swamp13Bottom': 'Swamp14',
    'Swamp13Left': 'Swamp10',
    'Swamp13Top1': 'Swamp09',
    'Swamp13Top2': 'Swamp09',
    'Swamp14Bottom': 'Swamp08',
    'Swamp14Right': 'Swamp11',
    'Swamp14Top': 'Swamp13',
    'Swamp15Left': 'Swamp08',
    'Swamp15Right': 'Swamp12',
    'Swamp15Top': 'Swamp11',
    'Swamp16Left': 'Swamp17',
    'Swamp16Top': 'Swamp07',
    'Swamp17Left': 'Swamp18',
    'Swamp17Right': 'Swamp16',
    'Swamp18Bottom': 'Abyss01',
    'Swamp18Right': 'Swamp17',

    'Village01Bottom': 'Church08',
    'Village01Right': 'Village02',
    'Village02Bottom': 'Village13',
    'Village02Left': 'Village01',
    'Village02Right': 'Village03',
    'Village03Bottom1': 'Village02',
    'Village03Bottom2': 'Village13',
    'Village03Right': 'Village05',
    'Village041Bottom': 'Village04',
    'Village04Right': 'Village05',
    'Village04Top': 'Village041',
    'Village05Left': 'Village03',
    'Village05Right': 'Village06',
    'Village05Top': 'Village04',
    'Village06Bottom': 'Village12',
    'Village06Left': 'Village05',
    'Village06Right1': 'Village07',
    'Village06Right2': 'Village08',
    'Village07Left': 'Village06',
    'Village07Right': 'Village09',
    'Village07Top': 'Village14',
    'Village08Left': 'Village06',
    'Village08Right': 'Village09',
    'Village09Left1': 'Village07',
    'Village09Left2': 'Village08',
    'Village09Right1': 'Village10',
    'Village09Right2': 'Village15',
    'Village10Left': 'Village09',
    'Village10Right': 'Village11',
    'Village111Bottom': 'Village11',
    'Village11Left': 'Village10',
    'Village11Right': 'Castle01',
    'Village11Top': 'Village111',
    'Village12Left1': 'Village13',
    'Village12Left2': 'Village16',
    'Village12Right': 'Cave01',
    'Village12Top': 'Village06',
    'Village13Left': 'Village02',
    'Village13Right': 'Village12',
    'Village13Top': 'Village03',
    'Village14Bottom': 'Village07',
    'Village15Left': 'Village09',
    'Village15Right': 'Fort01',
    'Village16Right': 'Village12',

}

map_location_to_alias = {}

# We need this since generated content should be hashable both ways
for key, value in map_alias_to_location.items():
    map_location_to_alias.update({value: key})

# print(map_location_to_alias)

# print(map_location_to_alias)
# Region = Room and need a list of rooms
region_rooms = []

room_exits = {}

# Regex because I'm lazy
pattern = re.compile(r"[A-Za-z]+[0-9]+", re.IGNORECASE)

for name in map_alias_to_location.keys():

    # Example Region Room = Abyss01
    region_room = pattern.match(name).group()

    # quick way to remove duplicates
    if region_room not in region_rooms:
        region_rooms.append(region_room)

    if region_room in name:
        # print(f"{name}:{region_room}")
        region_connector_name = region_connectors_lookup[name]
        if room_exits.get(region_room) is None:
            room_exits.update({region_room: [region_connector_name]})
        else:
            room_exits[region_room].append(region_connector_name)

nodes_alias_table = ds_data["nodes_alias"]

nodes_table = ds_data["nodes"]
