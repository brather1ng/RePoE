from functools import partial
import argparse

from RePoE.stat_descriptions import write_stat_descriptions
from RePoE.util import load_ggpk

if __name__ == '__main__':
    modules = {
        'stats': partial(write_stat_descriptions, data_path='../data/'),
        'mods': lambda g: None  # todo
    }

    parser = argparse.ArgumentParser(description="Convert GGPK files to Json using PyPoE")
    parser.add_argument('modules', metavar="module", nargs='+', choices=modules.keys(),
                        help="the converter modules to run (choose from '" + "', '".join(modules.keys()) + "')")
    parser.add_argument('-f', '--file', default='C:/Program Files (x86)/Grinding Gear Games/Path of Exile/Content.ggpk',
                        help="path to your Content.ggpk file")
    args = parser.parse_args()

    print("Loading GGPK ...", end='', flush=True)
    ggpk = load_ggpk(args.file)
    print(" Done!")

    for module in args.modules:
        print("Running module '", module, "'")
        modules[module](ggpk)
