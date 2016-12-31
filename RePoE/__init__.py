import argparse

from RePoE.mods import write_mods
from RePoE.stat_translations import write_stat_translations
from RePoE.stats import write_stats
from RePoE.util import load_ggpk, create_relational_reader

if __name__ == '__main__':
    modules = {
        'stat_translations': write_stat_translations,
        'mods': write_mods,
        'stats': write_stats
        # todo 'gems': SkillGems.dat or BaseItemTypes.dat
        # todo 'buffs': BuffDefinitions.dat?
        # todo 'master_crafting': CraftingBenchOptions.dat
        # todo 'essences': Essences.dat
        # todo GrantedEffects.dat and GrantedEffectsPerLevel.dat
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

    rr = create_relational_reader(ggpk)
    for module in args.modules:
        print("Running module '%s'" % module)
        modules[module](ggpk=ggpk, data_path='../data/', relational_reader=rr)
