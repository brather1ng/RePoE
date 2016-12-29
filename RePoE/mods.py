from PyPoE.poe.file import RelationalReader
from RePoE.util import load_ggpk, write_json


def _convert_stats(stats):
    # 'Stats' is a virtual field that is an array of ['Stat1', ..., 'Stat5'].
    # 'Stat{i}' is a virtual field that is an array of ['StatsKey{i}', 'Stat{i}Min', 'Stat{i}Max']
    r = []
    for stat in stats:
        if stat[0] is not None:
            r.append({
                'id': stat[0]['Id'],
                'min': stat[1],
                'max': stat[2]
            })
    return r


def _convert_spawn_weights(spawn_weights):
    # 'SpawnWeight' is a virtual field that is a tuple of ('SpawnWeight_TagsKeys', 'SpawnWeight_Values')
    r = []
    for tag, value in spawn_weights:
        r.append({
            tag['Id']: value > 0
        })
    return r


def _convert_buff(buff_definition, buff_value):
    if buff_definition is None:
        return {}
    return {
        'id': buff_definition['Id'],
        'range': buff_value
    }


def _convert_tags_keys(tags_keys):
    r = []
    for tag in tags_keys:
        r.append(tag['Id'])
    return r


DOMAINS = {
    1: "wearable_item",
    2: "flask",
    3: "monster",
    4: "chest",              # chests and strongboxes
    5: "area",               # areas and maps
    9: "monster_behaviour",  # e.g. StanceBanditRun
    10: "master_crafted",
    11: "jewel",
    12: "sextant"
}
GENERATION_TYPES = {
    1: "prefix",             # not necessarily craftable with orbs, e.g. monster mods or some sextant mods are prefixes
    2: "suffix",             # not necessarily craftable with orbs, e.g. monster mods
    3: "other",              # generic, not-craftable mod, e.g. unique explicits, item implicits, prophecies, ...
    4: "monster_nemesis",
    5: "item_corruption",
    6: "monster_bloodlines",
    7: "monster_torment",
    8: "map_tempest",
    9: "monster_talisman",
    10: "item_enchantment",
    11: "monster_essence"
}


# todo enable when useful
# ignored information about mods:
# - GenerationWeight_{TagsKeys, Values} (changes mod spawning weight when the item has specific tags, e.g. those above)
# - GrantedEffectsPerLevelKey (these have stat representations that can be worked with)
# ignored mods:
# - domain of 'monster', 'chest', 'area', 'monster_behaviour' and 'sextant'
def write_mods(ggpk, data_path):
    opt = {
        'use_dat_value': False,
        'auto_build_index': True,
    }
    rr = RelationalReader(path_or_ggpk=ggpk, files=['Mods.dat'], read_options=opt)

    root = {}
    for mod in rr['Mods.dat']:
        domain = DOMAINS[mod['Domain']]
        if (domain == "monster" or domain == "chest" or domain == "area" or domain == "monster_behaviour"
                or domain == "sextant"):
            continue
        obj = {
            'level': mod['Level'],
            'stats': _convert_stats(mod['Stats']),
            'domain': domain,
            'name': mod['Name'],
            'generation_type': GENERATION_TYPES[mod['GenerationType']],
            'group': mod['CorrectGroup'],
            'spawns_on': _convert_spawn_weights(mod['SpawnWeight']),
            'buff': _convert_buff(mod['BuffDefinitionsKey'], mod['BuffValue']),
            'is_essence_only': mod['IsEssenceOnlyModifier'] > 0,
            'adds_tags': _convert_tags_keys(mod['TagsKeys'])
        }
        if mod['Id'] in root:
            print("Duplicate mod id:", mod['Id'])
        else:
            root[mod['Id']] = obj

    write_json(root, data_path, 'mods')


if __name__ == '__main__':
    ggpk = load_ggpk('C:/Program Files (x86)/Grinding Gear Games/Path of Exile/Content.ggpk')
    write_mods(ggpk, '../data/')
