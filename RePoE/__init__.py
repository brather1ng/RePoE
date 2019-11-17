import json
import os


def _get_file_path_from_data_dir(file_name):
    this_dir, _ = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "data", file_name)
    return DATA_PATH


def _get_all_json_files():
    json_files = [
        pos_json
        for pos_json in os.listdir(_get_file_path_from_data_dir(""))
        if pos_json.endswith(".json") and not pos_json.endswith(".min.json")
    ]
    return json_files


def add_jsons_to_global():
    for json_string in _get_all_json_files():
        file_path = _get_file_path_from_data_dir(json_string)
        with open(file_path) as json_data:
            try:
                globals()[json_string[:-5]] = json.load(json_data)
            except json.decoder.JSONDecodeError:
                print(
                    f"Warning: {json_string} failed to decode json \n Recommended to execute run_parser.py to fix"
                )


add_jsons_to_global()

if __name__ == "__main__":
    print(characters)
