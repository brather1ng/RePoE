import argparse

from RePoE.crafting_bench_options import write_crafting_bench_options
from RePoE.gem_tags import write_gem_tags
from RePoE.gems import write_gems
from RePoE.mods import write_mods
from RePoE.npc_master import write_npc_master
from RePoE.stat_translations import write_stat_translations
from RePoE.stats import write_stats
from RePoE.util import load_ggpk, create_relational_reader, create_translation_file_cache


def main(data_path='../data/'):
    modules = {
        'stat_translations': write_stat_translations,
        'mods': write_mods,
        'stats': write_stats,
        'gems': write_gems,  # gems.json and gem_tooltips.json
        'gem_tags': write_gem_tags,
        'crafting_bench_options': write_crafting_bench_options,
        'npc_master': write_npc_master,
        # todo maybe Essences.dat
        # todo 'buffs': BuffDefinitions.dat?
    }

    parser = argparse.ArgumentParser(description="Convert GGPK files to Json using PyPoE")
    parser.add_argument('modules', metavar="module", nargs='+', choices=modules.keys(),
                        help="the converter modules to run (choose from '" + "', '".join(modules.keys()) + "')")
    parser.add_argument('-f', '--file', default='D:/Program Files (x86)/Grinding Gear Games/Path of Exile/Content.ggpk',
                        help="path to your Content.ggpk file")
    args = parser.parse_args()

    print("Loading GGPK ...", end='', flush=True)
    ggpk = load_ggpk(args.file)
    print(" Done!")

    rr = create_relational_reader(ggpk)
    tfc = create_translation_file_cache(ggpk)
    for module in args.modules:
        print("Running module '%s'" % module)
        modules[module](ggpk=ggpk, data_path=data_path, relational_reader=rr, translation_file_cache=tfc)

if __name__ == '__main__':
    main()
