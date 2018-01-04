from RePoE.util import call_with_default_args, write_json


def write_tags(data_path, relational_reader, **kwargs):
    tags = [row['Id'] for row in relational_reader['Tags.dat']]
    write_json(tags, data_path, 'tags')


if __name__ == '__main__':
    call_with_default_args(write_tags)
