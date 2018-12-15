import itertools

from RePoE.util import write_json, call_with_default_args


def write_crafting_bench_options(data_path, relational_reader, **kwargs):
    root = []
    for row in relational_reader['CraftingBenchOptions.dat']:
        if row['ModsKey'] is None or row['RequiredLevel'] > 100:
            continue
        item_class_row_lists = [categories['ItemClassesKeys'] for categories in row['CraftingItemClassCategoriesKeys']]
        item_class_rows = itertools.chain.from_iterable(item_class_row_lists)
        item_classes = [item_class['Id'] for item_class in item_class_rows]
        root.append({
            'master': row['HideoutNPCsKey']['NPCMasterKey']['Id'],
            'mod_id': row['ModsKey']['Id'],
            'bench_group': row['ModFamily'],
            'bench_tier': row['Tier'],
            'item_classes': item_classes,
        })
    write_json(root, data_path, 'crafting_bench_options')


if __name__ == '__main__':
    call_with_default_args(write_crafting_bench_options)
