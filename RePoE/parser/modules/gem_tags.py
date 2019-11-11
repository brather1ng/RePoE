from RePoE.parser.util import write_json, call_with_default_args


def write(data_path, relational_reader, **kwargs):
    root = {}
    for tag in relational_reader['GemTags.dat']:
        name = tag['Tag']
        root[tag['Id']] = name if name != '' else None
    write_json(root, data_path, 'gem_tags')


if __name__ == '__main__':
    call_with_default_args(write)
