import argparse
import importlib
import RePoE

from RePoE.parser.util import load_ggpk, create_relational_reader, create_translation_file_cache, \
    DEFAULT_GGPK_PATH, create_ot_file_cache


def main(data_path='../data/'):

    modules = RePoE.modules
    parser = argparse.ArgumentParser(description="Convert GGPK files to Json using PyPoE")
    parser.add_argument('modules', metavar="module", nargs='+', choices=modules,
                        help="the converter modules to run (choose from '" + "', '".join(modules) + "')")
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
    for module_string in selected_modules:
        print("Running module '%s'" % module_string)
        module = importlib.import_module(f"RePoE.parser.modules.{module_string}")
        module.write(ggpk=ggpk, data_path=data_path, relational_reader=rr,
                        translation_file_cache=tfc, ot_file_cache=otfc)


if __name__ == '__main__':
    main()