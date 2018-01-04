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
    # One hand melee classes and two hand melee classes each have the same essence mods.
    # The distribution of the 1Hand_ModsKey{2-8} and 2Hand_ModsKey{2-5} keys is arbitrary.
    class_to_key = {
        'Amulet': 'Amulet2_ModsKey',
        'Belt': 'Belt2_ModsKey',
        'Body Armour': 'BodyArmour2_ModsKey',
        'Boots': 'Boots2_ModsKey',
        'Bow': 'Bow_ModsKey',
        'Claw': '1Hand_ModsKey2',
        'Dagger': '1Hand_ModsKey3',
        'Gloves': 'Gloves2_ModsKey',
        'Helmet': 'Helmet2_ModsKey',
        'One Hand Axe': '1Hand_ModsKey4',
        'One Hand Mace': '1Hand_ModsKey5',
        'One Hand Sword': '1Hand_ModsKey6',
        'Quiver': 'Quiver_ModsKey',
        'Ring': 'Ring_ModsKey',
        'Sceptre': '1Hand_ModsKey7',
        'Shield': 'Shield2_ModsKey',
        'Staff': '2Hand_ModsKey2',
        'Thrusting One Hand Sword': '1Hand_ModsKey8',
        'Two Hand Axe': '2Hand_ModsKey3',
        'Two Hand Mace': '2Hand_ModsKey4',
        'Two Hand Sword': '2Hand_ModsKey5',
        'Wand': 'Wand_ModsKey',
    }
    return {
        item_class: row[key]['Id']
        for item_class, key in class_to_key.items() if row[key] is not None
    }


if __name__ == '__main__':
    call_with_default_args(write_essences)
