import json
import io

from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache
from PyPoE.poe.constants import MOD_DOMAIN

from RePoE import __DATA_PATH__
from RePoE.parser.constants import (
    UNRELEASED_ITEMS,
    ReleaseState,
    LEGACY_ITEMS,
    UNIQUE_ONLY_ITEMS,
    STAT_DESCRIPTION_NAMING_EXCEPTIONS,
)


def get_id_or_none(relational_file_cell):
    return None if relational_file_cell is None else relational_file_cell["Id"]


def write_json(root_obj, data_path, file_name):
    print("Writing '" + str(file_name) + ".json' ...", end="", flush=True)
    json.dump(root_obj, io.open(data_path + file_name + ".json", mode="w"), indent=2, sort_keys=True)
    print(" Done!")
    print("Writing '" + str(file_name) + ".min.json' ...", end="", flush=True)
    json.dump(root_obj, io.open(data_path + file_name + ".min.json", mode="w"), separators=(",", ":"), sort_keys=True)
    print(" Done!")


def load_file_system(ggpk_path):
    return FileSystem(ggpk_path)


def create_relational_reader(file_system):
    opt = {
        "use_dat_value": False,
        "auto_build_index": True,
    }
    return RelationalReader(path_or_file_system=file_system, files=["Stats.dat"], read_options=opt)


def create_translation_file_cache(file_system):
    return TranslationFileCache(path_or_file_system=file_system)


def create_ot_file_cache(file_system):
    return OTFileCache(path_or_file_system=file_system)


DEFAULT_GGPK_PATH = "C:/Program Files (x86)/Grinding Gear Games/Path of Exile"


def call_with_default_args(write_func):
    file_system = load_file_system(DEFAULT_GGPK_PATH)
    return write_func(
        file_system=file_system,
        data_path=__DATA_PATH__,
        relational_reader=create_relational_reader(file_system),
        translation_file_cache=create_translation_file_cache(file_system),
        ot_file_cache=create_ot_file_cache(file_system),
    )


def get_release_state(item_id):
    if item_id in UNRELEASED_ITEMS:
        return ReleaseState.unreleased
    if item_id in LEGACY_ITEMS:
        return ReleaseState.legacy
    if item_id in UNIQUE_ONLY_ITEMS:
        return ReleaseState.unique_only
    return ReleaseState.released


def ignore_mod_domain(domain):
    whitelist = {
        MOD_DOMAIN.ITEM,
        MOD_DOMAIN.FLASK,
        MOD_DOMAIN.AREA,
        MOD_DOMAIN.CRAFTED,
        MOD_DOMAIN.MISC,
        MOD_DOMAIN.ATLAS,
        MOD_DOMAIN.ABYSS_JEWEL,
        MOD_DOMAIN.DELVE,
        MOD_DOMAIN.AFFLICTION_JEWEL,
        MOD_DOMAIN.WATCHSTONE,
        MOD_DOMAIN.VEILED,
    }
    return domain not in whitelist


def get_stat_translation_file_name(game_file):
    if game_file in STAT_DESCRIPTION_NAMING_EXCEPTIONS:
        return f"stat_translations{STAT_DESCRIPTION_NAMING_EXCEPTIONS[game_file]}"
    elif game_file.endswith("_stat_descriptions.txt"):
        suffix_length = len("_stat_descriptions.txt")
        return f"stat_translations/{game_file[:-suffix_length]}"
    elif game_file.endswith("descriptions.txt"):
        raise ValueError(
            f"The following stat description file name is not accounted for: {game_file},"
            + " please add it to STAT_DESCRIPTION_NAMING_EXCEPTIONS in constants.py or add a generalized case to"
            + " util.py::get_stat_translation_file_name"
        )
    else:
        return None
