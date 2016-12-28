from functools import partial
import argparse

from RePoE.mods import write_mods
from RePoE.stat_translations import write_stat_translations
from RePoE.util import load_ggpk

if __name__ == '__main__':
    modules = {
        'stat_translations': partial(write_stat_translations, data_path='../data/'),
        'mods': partial(write_mods, data_path='../data/')
        # todo 'stats': Stats.dat: Id, IsLocal, IsWeaponLocal, maybe find out what other flags do
        # todo 'buffs': BuffDefinitions.dat?
        # todo 'master_crafting': CraftingBenchOptions.dat
        # todo 'essences': Essences.dat
        # todo 'tags': Tags.dat (just an array of the tag ids)
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
