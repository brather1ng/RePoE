import json

import os

#RePoe.modules
modules = ['stat_translations', 'mods', 'stats', 'gems', 'gem_tags', 'crafting_bench_options', 'base_items', 'tags', 'item_classes', 'essences', 'default_monster_stats', 'characters', 'fossils', 'mod_types']


def _get_file_path_from_data_dir(file_name):
    this_dir, _ = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data", file_name)
    return DATA_PATH

def add_modules_to_local():
    for module_string in modules:
        file_path = _get_file_path_from_data_dir(f"{module_string}.json")
        with open(file_path) as json_data:
            locals()[module_string] = json.load(json_data)

add_modules_to_local()