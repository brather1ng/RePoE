import json
from RePoE.parser.modules import get_parser_modules
import os

def _get_file_path_from_data_dir(file_name):
    this_dir, _ = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data", file_name)
    return DATA_PATH


#TODO: automatically take all json and add to locals.
def add_modules_to_local():
    for module_string in get_parser_modules():
        file_path = _get_file_path_from_data_dir(f"{module_string}.json")
        with open(file_path) as json_data:
            locals()[module_string] = json.load(json_data)

add_modules_to_local()