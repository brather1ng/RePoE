from RePoE.util import call_with_default_args, write_json


def write_synthesis_corrupted_implicits(data_path, relational_reader, **kwargs):
    data = {
        row['ItemClassesKey']['Id']:
            [mod['Id'] for mod in row['ModsKeys']]
        for row in relational_reader['ItemSynthesisCorruptedMods.dat']
    }
    write_json(data, data_path, 'synthesis_corrupted_implicits')


if __name__ == '__main__':
    call_with_default_args(write_synthesis_corrupted_implicits)
