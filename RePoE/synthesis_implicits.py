from RePoE.util import call_with_default_args, write_json


def write_synthesis_implicits(data_path, relational_reader, **kwargs):
    data = [
        {
            'stat': {
                'id': row['StatsKey']['Id'],
                'value': row['StatValue'],
            },
            'item_classes': [item_class['Id'] for item_class in row['ItemClassesKeys']],
            'mods': [mod['Id'] for mod in row['ModsKeys']],
        } for row in relational_reader['ItemSynthesisMods.dat']
    ]
    write_json(data, data_path, 'synthesis_implicits')


if __name__ == '__main__':
    call_with_default_args(write_synthesis_implicits)
