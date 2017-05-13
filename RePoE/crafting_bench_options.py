from RePoE.util import write_json, call_with_default_args


def write_crafting_bench_options(data_path, relational_reader, **kwargs):
    root = []
    for row in relational_reader['CraftingBenchOptions.dat']:
        if row['ModsKey'] is None:
            continue
        obj = {
            'mod_id': row['ModsKey']['Id'],
            'master_id': row['NPCMasterKey']['Id'],
            'master_level': row['MasterLevel'],
            'item_classes': [item_class['Id'] for item_class in row['ItemClassesKeys']]
        }
        root.append(obj)
    write_json(root, data_path, 'crafting_bench_options')


if __name__ == '__main__':
    call_with_default_args(write_crafting_bench_options)
