from collections import defaultdict

from RePoE.parser import Parser_Module
from RePoE.parser.constants import UNRELEASED_ITEMS, ReleaseState, LEGACY_ITEMS, UNIQUE_ONLY_ITEMS
from RePoE.parser.util import write_json, call_with_default_args, get_release_state


def _create_default_dict(relation):
    d = {row['BaseItemTypesKey']['Id']: row
         for row in relation if row['BaseItemTypesKey'] is not None}
    return defaultdict(lambda: None, d)


def _add_if_greater_zero(value, key, obj):
    if value > 0:
        obj[key] = value


def _add_if_not_zero(value, key, obj):
    if value != 0:
        obj[key] = value


def _convert_requirements(attribute_requirements, drop_level):
    if attribute_requirements is None:
        return None
    return {
        'strength': attribute_requirements['ReqStr'],
        'dexterity': attribute_requirements['ReqDex'],
        'intelligence': attribute_requirements['ReqInt'],
        'level': drop_level
    }


def _convert_armour_properties(armour_row, properties):
    if armour_row is None:
        return
    _add_if_greater_zero(armour_row['Armour'], 'armour', properties)
    _add_if_greater_zero(armour_row['Evasion'], 'evasion', properties)
    _add_if_greater_zero(armour_row['EnergyShield'], 'energy_shield', properties)
    _add_if_not_zero(armour_row['IncreasedMovementSpeed'], 'movement_speed', properties)


def _convert_shield_properties(shield_row, properties):
    if shield_row is None:
        return
    properties['block'] = shield_row['Block']


def _convert_flask_properties(flask_row, properties):
    if flask_row is None:
        return
    _add_if_greater_zero(flask_row['LifePerUse'], 'life_per_use', properties)
    _add_if_greater_zero(flask_row['ManaPerUse'], 'mana_per_use', properties)
    _add_if_greater_zero(flask_row['RecoveryTime'], 'duration', properties)


def _convert_flask_buff(flask_row, item_object):
    if flask_row is None or flask_row['BuffDefinitionsKey'] is None:
        return None
    stats_values = zip(flask_row['BuffDefinitionsKey']['StatsKeys'], flask_row['BuffStatValues'])
    item_object['grants_buff'] = {
        'id': flask_row['BuffDefinitionsKey']['Id'],
        'stats': {},
    }
    for (stat, value) in stats_values:
        item_object['grants_buff']['stats'][stat['Id']] = value


def _convert_flask_charge_properties(flask_row, properties):
    if flask_row is None:
        return
    properties['charges_max'] = flask_row['MaxCharges']
    properties['charges_per_use'] = flask_row['PerCharge']


def _convert_weapon_properties(weapon_row, properties):
    if weapon_row is None:
        return
    properties['critical_strike_chance'] = weapon_row['Critical']
    properties['attack_time'] = weapon_row['Speed']
    properties['physical_damage_min'] = weapon_row['DamageMin']
    properties['physical_damage_max'] = weapon_row['DamageMax']
    properties['range'] = weapon_row['RangeMax']


def _convert_currency_properties(currency_row, properties):
    if currency_row is None:
        return
    properties['stack_size'] = currency_row['Stacks']
    properties['directions'] = currency_row['Directions']
    if currency_row['FullStack_BaseItemTypesKey']:
        properties['full_stack_turns_into'] = currency_row['FullStack_BaseItemTypesKey']['Id']
    properties['description'] = currency_row['Description']
    properties['stack_size_currency_tab'] = currency_row['CurrencyTab_StackSize']




ITEM_CLASS_WHITELIST = {
    "LifeFlask", "ManaFlask", "HybridFlask", "Currency", "Amulet", "Ring", "Claw", "Dagger", "Rune Dagger",
    "Wand", "One Hand Sword", "Thrusting One Hand Sword", "One Hand Axe", "One Hand Mace", "Bow",
    "Staff", "Warstaff", "Two Hand Sword", "Two Hand Axe", "Two Hand Mace", "Active Skill Gem",
    "Support Skill Gem", "Quiver", "Belt", "Gloves", "Boots", "Body Armour", "Helmet", "Shield",
    "StackableCurrency", "Sceptre", "UtilityFlask", "UtilityFlaskCritical", "FishingRod",
    "Jewel", "AbyssJewel", "DivinationCard",
}

class base_items(Parser_Module):

    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        attribute_requirements = \
            _create_default_dict(relational_reader['ComponentAttributeRequirements.dat'])
        armour_types = _create_default_dict(relational_reader['ComponentArmour.dat'])
        shield_types = _create_default_dict(relational_reader['ShieldTypes.dat'])
        flask_types = _create_default_dict(relational_reader['Flasks.dat'])
        flask_charges = _create_default_dict(relational_reader['ComponentCharges.dat'])
        weapon_types = _create_default_dict(relational_reader['WeaponTypes.dat'])
        currency_type = _create_default_dict(relational_reader['CurrencyItems.dat'])
        # Not covered here: SkillGems.dat (see gems.py), Essences.dat (see essences.py)

        root = {}
        for item in relational_reader['BaseItemTypes.dat']:
            if item['ItemClassesKey']['Id'] not in ITEM_CLASS_WHITELIST:
                continue

            inherited_tags = list(ot_file_cache[item['InheritsFrom'] + '.ot']['Base']['tag'])
            item_id = item['Id']
            properties = {}
            _convert_armour_properties(armour_types[item_id], properties)
            _convert_shield_properties(shield_types[item_id], properties)
            _convert_flask_properties(flask_types[item_id], properties)
            _convert_flask_charge_properties(flask_charges[item_id], properties)
            _convert_weapon_properties(weapon_types[item_id], properties)
            _convert_currency_properties(currency_type[item_id], properties)
            root[item_id] = {
                'name': item['Name'],
                'item_class': item['ItemClassesKey']['Id'],
                'inventory_width': item['Width'],
                'inventory_height': item['Height'],
                'drop_level': item['DropLevel'],
                'implicits': [mod['Id'] for mod in item['Implicit_ModsKeys']],
                'tags': [tag['Id'] for tag in item['TagsKeys']] + inherited_tags,
                'visual_identity': {
                    'id': item['ItemVisualIdentityKey']['Id'],
                    'dds_file': item['ItemVisualIdentityKey']['DDSFile'],
                },
                'requirements':
                    _convert_requirements(attribute_requirements[item_id], item['DropLevel']),
                'properties': properties,
                'release_state': get_release_state(item_id).name,
                'domain': item['ModDomainsKey'].name.lower(),
            }
            _convert_flask_buff(flask_types[item_id], root[item_id])

        write_json(root, data_path, 'base_items')


if __name__ == '__main__':
    call_with_default_args(base_items.write)