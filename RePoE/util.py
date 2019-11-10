import json
import io

from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.ggpk import GGPKFile
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


def get_id_or_none(relational_file_cell):
    return None if relational_file_cell is None else relational_file_cell['Id']


def write_json(root_obj, data_path, file_name):
    print("Writing '" + str(file_name) + ".json' ...", end='', flush=True)
    json.dump(root_obj, io.open(data_path + file_name + '.json', mode='w'), indent=2, sort_keys=True)
    print(" Done!")
    print("Writing '" + str(file_name) + ".min.json' ...", end='', flush=True)
    json.dump(root_obj, io.open(data_path + file_name + '.min.json', mode='w'), separators=(',', ':'), sort_keys=True)
    print(" Done!")


def load_ggpk(ggpk_path):
    ggpk = GGPKFile()
    ggpk.read(ggpk_path)
    ggpk.directory_build()
    return ggpk


def create_relational_reader(ggpk):
    opt = {
        'use_dat_value': False,
        'auto_build_index': True,
    }
    return RelationalReader(path_or_ggpk=ggpk, files=['Stats.dat'], read_options=opt)


def create_translation_file_cache(ggpk):
    return TranslationFileCache(path_or_ggpk=ggpk)


def create_ot_file_cache(ggpk):
    return OTFileCache(path_or_ggpk=ggpk)


DEFAULT_GGPK_PATH = 'C:/Program Files (x86)/Grinding Gear Games/Path of Exile/Content.ggpk'


def call_with_default_args(write_func):
    ggpk = load_ggpk(DEFAULT_GGPK_PATH)
    write_func(ggpk=ggpk, data_path='../data/', relational_reader=create_relational_reader(ggpk),
               translation_file_cache=create_translation_file_cache(ggpk),
               ot_file_cache=create_ot_file_cache(ggpk))
