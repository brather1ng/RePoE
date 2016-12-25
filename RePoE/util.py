import json
import io

from PyPoE.poe.file import GGPKFile


def write_json(root_obj, data_path, file_name):
    print("Writing '", file_name, ".json' ...")
    json.dump(root_obj, io.open(data_path + file_name + '.json', mode='w'), indent=2, sort_keys=True)
    print("Writing '", file_name, ".min.json' ...")
    json.dump(root_obj, io.open(data_path + file_name + '.min.json', mode='w'), separators=(',', ':'))


def load_ggpk(ggpk_path):
    ggpk = GGPKFile()
    ggpk.read(ggpk_path)
    ggpk.directory_build()
    return ggpk
