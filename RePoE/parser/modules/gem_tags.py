from RePoE.parser import Parser_Module
from RePoE.parser.util import write_json, call_with_default_args

class gem_tags(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        for tag in relational_reader['GemTags.dat']:
            name = tag['Tag']
            root[tag['Id']] = name if name != '' else None
        write_json(root, data_path, 'gem_tags')


if __name__ == '__main__':
    call_with_default_args(gem_tags.write)
