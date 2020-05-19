from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module


class cluster_jewels(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        skills = {}
        for row in relational_reader['PassiveTreeExpansionSkills.dat']:
            size = row['PassiveTreeExpansionJewelSizesKey']['Name']
            if size not in skills:
                skills[size] = []
            skills[size].append({
                'id': row['PassiveSkillsKey']['Id'],
                'name': row['PassiveSkillsKey']['Name'],
                'stats': {stat['Id']: value for stat, value in row['PassiveSkillsKey']['Stats']},
                'tag': row['TagsKey']['Id']
            })

        data = {}
        for row in relational_reader['PassiveTreeExpansionJewels.dat']:
            size = row['PassiveTreeExpansionJewelSizesKey']['Name']
            data[row['BaseItemTypesKey']['Id']] = {
                'name': row['BaseItemTypesKey']['Name'],
                'size': size,
                'min_skills': row['MinNodes'],
                'max_skills': row['MaxNodes'],
                'small_indices': row['SmallIndices'],
                'notable_indices': row['NotableIndices'],
                'socket_indices': row['SocketIndices'],
                'total_indices': row['TotalIndices'],
                'passive_skills': skills[size]
            }
        write_json(data, data_path, 'cluster_jewels')


if __name__ == '__main__':
    call_with_default_args(cluster_jewels.write)
