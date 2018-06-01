from RePoE.util import call_with_default_args, write_json


def write_essences(data_path, relational_reader, **kwargs):
    essences = {
        row['BaseItemTypesKey']['Id']: {
            'name': row['BaseItemTypesKey']['Name'],
            'spawn_level_min': row['DropLevelMinimum'],
            'spawn_level_max': row['DropLevelMaximum'],
            'level': row['Tier'],
            'item_level_restriction':
                row['ItemLevelRestriction'] if row['ItemLevelRestriction'] > 0 else None,
            'type': {
                'tier': row['EssenceTypeKey']['EssenceType'],
                'is_corruption_only': row['EssenceTypeKey']['IsCorruptedEssence'],
            },
            'mods': _convert_mods(row)
        }
        for row in relational_reader['Essences.dat']
    }
    write_json(essences, data_path, 'essences')


def _convert_mods(row):
    class_to_key = {
        'Amulet': 'Amulet_ModsKey',
        'Belt': 'Belt_ModsKey',
        'Body Armour': 'BodyArmour_ModsKey',
        'Boots': 'Boots_ModsKey',
        'Bow': 'Bow_ModsKey',
        'Claw': 'Claw_ModsKey',
        'Dagger': 'Dagger_ModsKey',
        'Gloves': 'Gloves_ModsKey',
        'Helmet': 'Helmet_ModsKey',
        'One Hand Axe': '1HandAxe_ModsKey',
        'One Hand Mace': '1HandMace_ModsKey',
        'One Hand Sword': '1HandSword_ModsKey',
        'Quiver': 'Quiver_ModsKey',
        'Ring': 'Ring_ModsKey',
        'Sceptre': 'Sceptre_ModsKey',
        'Shield': 'Shield_ModsKey',
        'Staff': 'Staff_ModsKey',
        'Thrusting One Hand Sword': '1HandThrustingSword_ModsKey',
        'Two Hand Axe': '2HandAxe_ModsKey',
        'Two Hand Mace': '2HandMace_ModsKey',
        'Two Hand Sword': '2HandSword_ModsKey',
        'Wand': 'Wand_ModsKey',
    }
    return {
        item_class: row[key]['Id']
        for item_class, key in class_to_key.items() if row[key] is not None
    }


if __name__ == '__main__':
    call_with_default_args(write_essences)
