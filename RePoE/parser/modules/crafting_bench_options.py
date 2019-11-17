import itertools

from RePoE.parser import Parser_Module
from RePoE.parser.util import write_json, call_with_default_args


class crafting_bench_options(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
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
                'cost': {base_item['Id']: value for base_item, value in row['Cost']},
            })
        write_json(root, data_path, 'crafting_bench_options')


if __name__ == '__main__':
    call_with_default_args(crafting_bench_options.write)
