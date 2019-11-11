import json

import os

#RePoe.modules
modules = ['stat_translations', 'mods', 'stats', 'gems', 'gem_tags', 'crafting_bench_options', 'base_items', 'tags', 'item_classes', 'essences', 'default_monster_stats', 'characters', 'fossils', 'mod_types']


def _get_file_path_from_data_dir(file_name):
    this_dir, _ = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data", file_name)
    return DATA_PATH

def _generate_json_return_func(json_name):
    '''
    generates a python function which loads and returns the json located in data/
    '''
    def foo():
        file_path = _get_file_path_from_data_dir(f"{json_name}.json")
        with open(file_path) as json_data:
            return json.load(json_data)
    return foo

# adds functions for each module which when called return the json file
# example use: RePoE.mods() returns a python dict which contains the contents of data/mods.json
# we use a function call here instead of storing the dict to force the end user to 
# reload the json file incase it has been updated.
for module_string in modules:
    locals()[module_string] = _generate_json_return_func(module_string)