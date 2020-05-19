from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module


class cluster_jewel_notables(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        data = []
        for row in relational_reader['PassiveTreeExpansionSpecialSkills.dat']:
            data.append({
                'id': row['PassiveSkillsKey']['Id'],
                'name': row['PassiveSkillsKey']['Name'],
                'jewel_stat': row['StatsKey']['Id'],
            })
        write_json(data, data_path, 'cluster_jewel_notables')


if __name__ == '__main__':
    call_with_default_args(cluster_jewel_notables.write)
