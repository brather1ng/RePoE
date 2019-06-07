from PyPoE.poe.constants import MOD_DOMAIN
from RePoE.util import write_json, call_with_default_args


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
    # 'SpawnWeight' is a virtual field that is a zipped tuple of
    # ('SpawnWeight_TagsKeys', 'SpawnWeight_Values')
    r = []
    for tag, weight in spawn_weights:
        r.append({
            'tag': tag['Id'],
            'weight': weight
        })
    return r


def _convert_generation_weights(generation_weights):
    # 'GenerationWeight' is a virtual field that is a tuple of
    # ('GenerationWeight_TagsKeys', 'GenerationWeight_Values')
    r = []
    for tag, weight in generation_weights:
        r.append({
            'tag': tag['Id'],
            'weight': weight
        })
    return r


def _convert_buff(buff_definition, buff_value):
    if buff_definition is None:
        return {}
    return {
        'id': buff_definition['Id'],
        'range': buff_value
    }


def _convert_granted_effects(granted_effects_per_level):
    if granted_effects_per_level is None:
        return {}
    # These two identify a row in GrantedEffectsPerLevel.dat
    return [{
        'granted_effect_id': gepl['GrantedEffectsKey']['Id'],
        'level': gepl['Level']
    } for gepl in granted_effects_per_level]


def _convert_tags_keys(tags_keys):
    r = []
    for tag in tags_keys:
        r.append(tag['Id'])
    return r


def ignore_mod_domain(domain):
    whitelist = {
        MOD_DOMAIN.ITEM, MOD_DOMAIN.FLASK, MOD_DOMAIN.AREA, MOD_DOMAIN.CRAFTED, MOD_DOMAIN.MISC,
        MOD_DOMAIN.ATLAS, MOD_DOMAIN.ABYSS_JEWEL, MOD_DOMAIN.DELVE
    }
    return domain not in whitelist


# todo enable when useful
# ignored mods:
# - domain of 'monster', 'chest', 'stance', 'leaguestone'
def write_mods(data_path, relational_reader, **kwargs):
    root = {}
    for mod in relational_reader['Mods.dat']:
        domain = MOD_DOMAIN_FIX.get(mod['Id'], mod['Domain'])
        if ignore_mod_domain(domain):
            continue
        obj = {
            'required_level': mod['Level'],
            'stats': _convert_stats(mod['Stats']),
            'domain': domain.name.lower(),
            'name': mod['Name'],
            'type': mod['ModTypeKey']['Name'],
            'generation_type': mod['GenerationType'].name.lower(),
            'group': mod['CorrectGroup'],
            'spawn_weights': _convert_spawn_weights(mod['SpawnWeight']),
            'generation_weights': _convert_generation_weights(mod['GenerationWeight']),
            'grants_buff': _convert_buff(mod['BuffDefinitionsKey'], mod['BuffValue']),
            'grants_effects': _convert_granted_effects(mod['GrantedEffectsPerLevelKeys']),
            'is_essence_only': mod['IsEssenceOnlyModifier'] > 0,
            'adds_tags': _convert_tags_keys(mod['TagsKeys'])
        }
        if mod['Id'] in root:
            print("Duplicate mod id:", mod['Id'])
        else:
            root[mod['Id']] = obj

    write_json(root, data_path, 'mods')


# a few unique item mods have the wrong mod domain so they wouldn't be added to the file without this
MOD_DOMAIN_FIX = {
    "AreaDamageUniqueBodyDexInt1": MOD_DOMAIN.ITEM,
    "ElementalResistancePerEnduranceChargeDescentShield1": MOD_DOMAIN.ITEM,
    "LifeGainOnEndurangeChargeConsumptionUniqueBodyStrInt6": MOD_DOMAIN.ITEM,
    "ReturningProjectilesUniqueDescentBow1": MOD_DOMAIN.ITEM,
}


if __name__ == '__main__':
    call_with_default_args(write_mods)
