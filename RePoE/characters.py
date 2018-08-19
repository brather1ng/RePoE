from RePoE.util import write_json, call_with_default_args


def write_characters(data_path, relational_reader, **kwargs):
    root = []
    for row in relational_reader['Characters.dat']:
        root.append({
            'metadata_id': row['Id'],
            'integer_id': row['IntegerId'],
            'name': row['Name'],
            'base_stats': {
                'life': row['BaseMaxLife'],
                'mana': row['BaseMaxMana'],
                'strength': row['BaseStrength'],
                'dexterity': row['BaseDexterity'],
                'intelligence': row['BaseIntelligence'],
                'unarmed': {
                    'attack_time': row['WeaponSpeed'],
                    'min_physical_damage': row['MinDamage'],
                    'max_physical_damage': row['MaxDamage'],
                    'range': row['MaxAttackDistance'],
                },
            },
        })
    write_json(root, data_path, 'characters')


if __name__ == '__main__':
    call_with_default_args(write_characters)
