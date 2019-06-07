import argparse

from RePoE.base_items import write_base_items
from RePoE.characters import write_characters
from RePoE.crafting_bench_options import write_crafting_bench_options
from RePoE.default_monster_stats import write_default_monster_stats
from RePoE.essences import write_essences
from RePoE.gem_tags import write_gem_tags
from RePoE.gems import write_gems
from RePoE.item_classes import write_item_classes
from RePoE.mods import write_mods
from RePoE.stat_translations import write_stat_translations
from RePoE.stats import write_stats
from RePoE.tags import write_tags
from RePoE.fossils import write_fossils
from RePoE.mod_types import write_types
from RePoE.util import load_ggpk, create_relational_reader, create_translation_file_cache, \
    DEFAULT_GGPK_PATH, create_ot_file_cache


def main(data_path='../data/'):
    modules = {
        'all': None,
        'stat_translations': write_stat_translations,
        'mods': write_mods,
        'stats': write_stats,
        'gems': write_gems,  # gems.json and gem_tooltips.json
        'gem_tags': write_gem_tags,
        'crafting_bench_options': write_crafting_bench_options,
        'base_items': write_base_items,
        'tags': write_tags,
        'item_classes': write_item_classes,
        'essences': write_essences,
        'default_monster_stats': write_default_monster_stats,
        'characters': write_characters,
        'fossils': write_fossils,
        'types': write_types,
        # todo 'buffs': BuffDefinitions.dat?
    }

    parser = argparse.ArgumentParser(description="Convert GGPK files to Json using PyPoE")
    parser.add_argument('modules', metavar="module", nargs='+', choices=modules.keys(),
                        help="the converter modules to run (choose from '" + "', '".join(modules.keys()) + "')")
    parser.add_argument('-f', '--file', default=DEFAULT_GGPK_PATH,
                        help="path to your Content.ggpk file")
    args = parser.parse_args()

    print("Loading GGPK ...", end='', flush=True)
    ggpk = load_ggpk(args.file)
    print(" Done!")

    selected_modules = args.modules
    if 'all' in selected_modules:
        selected_modules = [m for m in modules if m != 'all']

    rr = create_relational_reader(ggpk)
    tfc = create_translation_file_cache(ggpk)
    otfc = create_ot_file_cache(ggpk)
    for module in selected_modules:
        print("Running module '%s'" % module)
        modules[module](ggpk=ggpk, data_path=data_path, relational_reader=rr,
                        translation_file_cache=tfc, ot_file_cache=otfc)


if __name__ == '__main__':
    main()
