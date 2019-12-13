from RePoE.parser import Parser_Module
from RePoE.parser.util import write_json, call_with_default_args


class default_monster_stats(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        for row in relational_reader['DefaultMonsterStats.dat']:
            root[row['DisplayLevel']] = {
                'physical_damage': row['Damage'],
                'evasion': row['Evasion'],
                'accuracy': row['Accuracy'],
                'life': row['Life'],
                'ally_life': row['AllyLife'],
                'armour': row['Armour'],
            }
        write_json(root, data_path, 'default_monster_stats')


if __name__ == '__main__':
    call_with_default_args(default_monster_stats.write)
