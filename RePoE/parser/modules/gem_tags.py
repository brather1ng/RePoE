from RePoE.parser import Parser_Module
from RePoE.parser.util import write_json, call_with_default_args

class gem_tags(Parser_Module):
    @classmethod
    def write(data_path, relational_reader, **kwargs):
        root = {}
        for tag in relational_reader['GemTags.dat']:
            name = tag['Tag']
            root[tag['Id']] = name if name != '' else None
        write_json(root, data_path, 'gem_tags')


if __name__ == '__main__':
    call_with_default_args(gem_tags.write)
