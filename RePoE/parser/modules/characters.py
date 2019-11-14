from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser import Parser_Module

class characters(Parser_Module):
    
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
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
    call_with_default_args(characters.write)
