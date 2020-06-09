import argparse

import RePoE
from importlib import reload

from RePoE.parser.modules import get_parser_modules

from RePoE.parser.util import (
    load_ggpk,
    create_relational_reader,
    create_translation_file_cache,
    DEFAULT_GGPK_PATH,
    create_ot_file_cache,
)


def main(data_path="./data/"):

    modules = get_parser_modules()

    module_names = [module.__name__ for module in modules]
    module_names.append("all")
    parser = argparse.ArgumentParser(
        description="Convert GGPK files to Json using PyPoE"
    )
    parser.add_argument(
        "module_names",
        metavar="module",
        nargs="+",
        choices=module_names,
        help="the converter modules to run (choose from '"
        + "', '".join(module_names)
        + "')",
    )
    parser.add_argument(
        "-f", "--file", default=DEFAULT_GGPK_PATH, help="path to your Content.ggpk file"
    )
    args = parser.parse_args()

    print("Loading GGPK ...", end="", flush=True)
    ggpk = load_ggpk(args.file)
    print(" Done!")

    selected_module_names = args.module_names
    if "all" in selected_module_names:
        selected_module_names = [m for m in module_names if m != "all"]

    rr = create_relational_reader(ggpk)
    tfc = create_translation_file_cache(ggpk)
    otfc = create_ot_file_cache(ggpk)

    selected_modules = [m for m in modules if m.__name__ in selected_module_names]
    for parser_module in selected_modules:
        print("Running module '%s'" % parser_module.__name__)
        parser_module.write(
            ggpk=ggpk,
            data_path=data_path,
            relational_reader=rr,
            translation_file_cache=tfc,
            ot_file_cache=otfc,
        )

    # This forces the globals to be up to date with what we just parsed, in case someone uses `run_parser` within a script
    reload(RePoE)


if __name__ == "__main__":
    main()
