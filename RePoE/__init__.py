import json
import os

# directory that this __init__ file lives in
__REPOE_DIR__, _ = os.path.split(__file__)

# full path to ./data
__DATA_PATH__ = os.path.join(__REPOE_DIR__, "data", "")


def load_json(json_file_path):
    file_path = __DATA_PATH__ + f"{json_file_path}"
    with open(file_path) as json_data:
        try:
            return json.load(json_data)
        except json.decoder.JSONDecodeError:
            print(f"Warning: {json_file_path} failed to decode json \n Recommended to execute run_parser.py to fix")


base_items = load_json("base_items.json")
characters = load_json("characters.json")
crafting_bench_options = load_json("crafting_bench_options.json")
default_monster_stats = load_json("default_monster_stats.json")
essences = load_json("essences.json")
flavour = load_json("flavour.json")
fossils = load_json("fossils.json")
gems = load_json("gems.json")
gem_tags = load_json("gem_tags.json")
gem_tooltips = load_json("gem_tooltips.json")
item_classes = load_json("item_classes.json")
mods = load_json("mods.json")
mod_types = load_json("mod_types.json")
quest_rewards = load_json("quest_rewards.json")
stats = load_json("stats.json")
stat_translations = load_json("stat_translations.json")
tags = load_json("tags.json")
vendor_rewards = load_json("vendor_rewards.json")
cluster_jewels = load_json("cluster_jewels.json")
cluster_jewel_notables = load_json("cluster_jewel_notables.json")


def _get_all_json_files():
    """get all json files in /data"""
    json_files = [
        pos_json
        for pos_json in os.listdir(__DATA_PATH__)
        if pos_json.endswith(".json") and not pos_json.endswith(".min.json")
    ]
    return json_files


def _assert_all_json_files_accounted_for():
    json_files = _get_all_json_files()
    for json_file in json_files:
        json_file_stripped = json_file[:-5]
        assert (
            json_file_stripped in globals()
        ), f"the following json file needs to be added to __init__ load: {json_file}"


_assert_all_json_files_accounted_for()

if __name__ == "__main__":
    print(characters)
