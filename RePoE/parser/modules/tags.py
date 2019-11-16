from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module

class tags(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        tags = [row['Id'] for row in relational_reader['Tags.dat']]
        write_json(tags, data_path, 'tags')


if __name__ == '__main__':
    call_with_default_args(tags.write)
